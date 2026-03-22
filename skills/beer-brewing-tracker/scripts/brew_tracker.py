#!/usr/bin/env python3
import argparse, json, time, urllib.parse, urllib.request
from pathlib import Path

STATE_PATH = Path('/home/peter/.openclaw/workspace/memory/brew-session.json')
OPENCLAW_CONFIG = Path('/home/peter/.openclaw/openclaw.json')


def now():
    return int(time.time())


def load_state():
    if not STATE_PATH.exists():
        return None
    return json.loads(STATE_PATH.read_text())


def save_state(s):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(s, indent=2) + '\n')


def fmt_dur(sec):
    if sec is None:
        return "unknown"
    if sec < 0:
        sec = 0
    m, _ = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if d:
        return f"{d}d {h}h {m}m"
    if h:
        return f"{h}h {m}m"
    return f"{m}m"


def current_step(s):
    i = s['current_index']
    steps = s['recipe']['steps']
    return steps[i] if i < len(steps) else None


def arm_timer(s):
    st = current_step(s)
    if not st:
        s['due_at'] = None
        return
    dur = st.get('duration_min')
    s['due_at'] = now() + dur * 60 if isinstance(dur, int) else None


def reminder_text(s):
    st = current_step(s)
    if not st:
        return "✅ Brew session complete."
    n = s['current_index'] + 1
    total = len(s['recipe']['steps'])
    note = f"\nNote: {st['notes']}" if st.get('notes') else ""
    return (
        f"🔔 Brew reminder\n"
        f"Session: {s['name']}\n"
        f"Do now ({n}/{total}): {st['name']}{note}\n"
        f"When done: run 'done' to set the next timer automatically."
    )


def send_telegram(text, chat_id):
    if not OPENCLAW_CONFIG.exists():
        return False, 'openclaw config not found'
    cfg = json.loads(OPENCLAW_CONFIG.read_text())
    token = (((cfg.get('channels') or {}).get('telegram') or {}).get('botToken'))
    if not token:
        return False, 'telegram bot token missing in config'

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({'chat_id': str(chat_id), 'text': text}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            _ = r.read()
        return True, 'sent'
    except Exception as e:
        return False, str(e)


def cmd_start(args):
    recipe = json.loads(Path(args.recipe).read_text())
    s = {
        'name': args.name or recipe.get('recipe_name', 'Brew Session'),
        'started_at': now(),
        'recipe': recipe,
        'current_index': 0,
        'step_started_at': now(),
        'due_at': None,
        'completed': []
    }
    arm_timer(s)
    save_state(s)
    print(f"Started: {s['name']}")
    print(reminder_text(s))


def cmd_status(_args):
    s = load_state()
    if not s:
        print('No active brew session. Use start first.')
        return
    st = current_step(s)
    if not st:
        print('Session complete ✅')
        return

    elapsed = now() - s['step_started_at']
    rem = s['due_at'] - now() if s.get('due_at') else None

    print(f"Session: {s['name']}")
    print(f"Step {s['current_index']+1}/{len(s['recipe']['steps'])}: {st['name']}")
    if 'notes' in st:
        print(f"Notes: {st['notes']}")
    print(f"Elapsed: {fmt_dur(elapsed)}")
    if rem is not None:
        print(f"Remaining: {fmt_dur(rem)}")
        if rem <= 0:
            print("⚠️ Step timer is due now. Run 'remind' or do the step and run 'done'.")


def cmd_done(_args):
    s = load_state()
    if not s:
        print('No active brew session.')
        return
    st = current_step(s)
    if not st:
        print('Already complete ✅')
        return

    s['completed'].append({
        'index': s['current_index'],
        'name': st['name'],
        'completed_at': now()
    })
    s['current_index'] += 1
    s['step_started_at'] = now()
    arm_timer(s)
    save_state(s)

    nxt = current_step(s)
    print(f"Completed: {st['name']}")
    if nxt:
        print(reminder_text(s))
        if s.get('due_at'):
            print(f"Next timer set: {fmt_dur(s['due_at']-now())}")
    else:
        print('Session complete ✅')


def cmd_timeline(_args):
    s = load_state()
    if not s:
        print('No active brew session.')
        return

    done_idx = {x['index'] for x in s['completed']}
    for i, st in enumerate(s['recipe']['steps']):
        mark = '✅' if i in done_idx else ('➡️' if i == s['current_index'] else '⏳')
        dur = f" ({st['duration_min']} min)" if 'duration_min' in st else ''
        print(f"{mark} {i+1}. {st['name']}{dur}")


def cmd_remind(_args):
    s = load_state()
    if not s:
        print('No active brew session.')
        return
    print(reminder_text(s))


def cmd_watch(args):
    s = load_state()
    if not s:
        print('No active brew session.')
        return

    interval = max(10, int(args.poll_sec))
    print(f"Watching brew timers every {interval}s. Ctrl+C to stop.")
    last_sent_for_step = None
    try:
        while True:
            s = load_state()
            if not s:
                print('No active brew session.')
                return
            st = current_step(s)
            if not st:
                print('✅ Session complete.')
                return
            idx = s['current_index']
            due_at = s.get('due_at')
            if due_at and now() >= due_at and last_sent_for_step != idx:
                txt = reminder_text(s)
                print(txt)
                if args.telegram_chat_id:
                    ok, msg = send_telegram(txt, args.telegram_chat_id)
                    print(f"Telegram: {'ok' if ok else 'fail'} ({msg})")
                last_sent_for_step = idx
                if args.once:
                    return
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\nStopped watching.')


def cmd_reset(_args):
    if STATE_PATH.exists():
        STATE_PATH.unlink()
    print('Brew session reset.')


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)

    s = sub.add_parser('start')
    s.add_argument('--recipe', required=True)
    s.add_argument('--name')
    s.set_defaults(func=cmd_start)

    sub.add_parser('status').set_defaults(func=cmd_status)
    sub.add_parser('done').set_defaults(func=cmd_done)
    sub.add_parser('timeline').set_defaults(func=cmd_timeline)
    sub.add_parser('remind').set_defaults(func=cmd_remind)

    w = sub.add_parser('watch')
    w.add_argument('--poll-sec', default=30)
    w.add_argument('--once', action='store_true', help='exit after first reminder trigger')
    w.add_argument('--telegram-chat-id', help='Send due reminders to this Telegram chat id')
    w.set_defaults(func=cmd_watch)

    sub.add_parser('reset').set_defaults(func=cmd_reset)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
