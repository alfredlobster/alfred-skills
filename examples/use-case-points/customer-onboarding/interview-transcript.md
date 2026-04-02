# Sample Interview Transcript — Customer Onboarding Portal

## Stakeholder
- Name: Anna Jensen
- Role: Operations Manager

## Business Goal
Create a customer onboarding portal that lets an operations team register new customers, validate their data, and activate accounts faster with less manual re-entry.

## Interview Notes
**Q:** What starts the process?
**A:** An operations manager receives a signed customer agreement and starts onboarding.

**Q:** Who uses the system directly?
**A:** Operations managers. Sometimes finance validates billing details. The customer receives activation output but does not use the internal portal directly.

**Q:** What must already be true before onboarding starts?
**A:** The agreement must be signed and required company details must be available.

**Q:** What does success look like?
**A:** The customer account is created, billing profile is valid, and the account is activated.

**Q:** What normally happens?
**A:**
1. Operations enters customer details.
2. System validates required fields.
3. System checks whether the customer already exists.
4. Operations enters billing details.
5. Finance validation runs if billing data is unusual.
6. System creates the customer account.
7. System activates the account.
8. System sends confirmation to operations.

**Q:** What variations happen?
**A:**
- If the customer already exists, onboarding stops and operations gets a warning.
- If billing details fail validation, operations must correct them.
- If finance review is required, activation waits for finance approval.

**Q:** What can go wrong?
**A:**
- Missing mandatory fields
- Duplicate customer
- Billing validation failure
- Activation service unavailable

**Q:** Non-functional requirements?
**A:**
- Portal should respond quickly during normal business use.
- Access must be role-based.
- Changes should be auditable.
