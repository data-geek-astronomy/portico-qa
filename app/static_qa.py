# Static Q&A Mapping - Pre-defined answers from policy documents
# No API calls needed - completely offline

STATIC_QA_MAPPING = {
    # Question variations mapped to the same answer
    "what is the pet policy": {
        "answer": """Portico welcomes responsible pet owners with prior written approval.

KEY POINTS:
- Maximum 2 pets per unit (cats and dogs)
- Pet deposit: $300 per pet (refundable, unless damage occurs)
- Pet rent: $35/month per pet
- Pet fee at lease signing: $100 per pet (non-refundable)
- Pets must be contained in unit at all times
- All dogs must be on-leash in common areas
- Excessive barking (>10 min continuous) is a lease violation

PROHIBITED BREEDS:
- Pit Bulls, Rottweilers, German Shepherds (except service animals)
- Chow Chows, Akitas, Husky/Malamute mixes
- Any dog with history of aggression

SERVICE ANIMALS: Exempt from pet fees and breed restrictions. Emotional support animals require documentation and are subject to pet fees.""",
        "document": "pet_policy.md",
        "section": "Pet Policy"
    },

    "how do i submit a maintenance request": {
        "answer": """Submit maintenance requests via tenant portal or phone: 1-800-PORTICO

RESPONSE TIMES:
- Emergency (0-4 hours): No heat/AC, no water, gas smell, electrical hazard, roof leaks, broken locks, sewage backup
- Urgent (1-2 days): Appliance issues, plumbing leaks, pest problems, sliding door/window malfunction
- Standard (3-7 days): Paint, caulking, hinges, cabinet repairs, light fixtures, flooring

RESIDENT RESPONSIBILITIES:
- Grant access to unit at scheduled time (24-hour notice required)
- Unit must be accessible (not locked/blocked)
- Failure to grant access may mark request as complete

MAINTENANCE COVERS:
- Normal wear and tear (water heater failure after 10 years)

RESIDENT LIABLE FOR:
- Negligence (sink overflow from leaving faucet running)
- Intentional damage (broken window from throwing object)
- Pet damage (stained carpet from accidents)""",
        "document": "maintenance_sop.md",
        "section": "Maintenance SOP"
    },

    "what is the security deposit": {
        "answer": """Security deposits at Portico are handled as follows:

DEPOSIT AMOUNT:
- Standard security deposit: One month's rent (refundable)
- Damage assessment conducted at move-out
- Deductions made only for damage beyond normal wear and tear

NORMAL WEAR & TEAR (Covered by Portico):
- Faded paint
- Minor scuffs on walls
- Worn carpet in high-traffic areas
- Expected appliance aging

RESIDENT LIABILITY (Non-refundable deductions):
- Hole repairs beyond nail holes
- Broken windows or doors
- Stained or damaged carpet from accidents
- Appliance damage from misuse
- Deep cleaning if unit not returned clean

REFUND PROCESS:
- Move-out inspection completed within 14 days
- Itemized list provided if deductions made
- Remaining deposit refunded to forwarding address
- Disputes can be raised within 30 days""",
        "document": "security_deposit.md",
        "section": "Security Deposit Policy"
    },

    "what fair housing protections apply": {
        "answer": """Portico complies with all Fair Housing Act requirements:

PROTECTED CLASSES:
- Race or color
- National origin
- Religion
- Sex (including pregnancy, gender identity, sexual orientation)
- Disability
- Familial status (families with children)
- Age (for senior housing communities)

PROHIBITED PRACTICES:
- Denying housing based on protected class status
- Different terms/conditions based on protected class
- Steering (directing people to certain units/communities)
- Harassment based on protected class
- Discriminatory advertising
- Denying reasonable accommodations for disabilities

ACCESSIBILITY REQUIREMENTS:
- Common areas must be accessible to people with disabilities
- Accessible parking spaces required
- Ramps or alternative access to buildings
- Accessible entrances and elevators
- Accessible community facilities

REASONABLE ACCOMMODATIONS:
- Request submitted in writing to management
- Portico reviews and responds within 10 business days
- Examples: service animals, accessible parking, appliance modifications
- Requests processed fairly and timely

For discrimination complaints: Contact HUD at 1-800-669-9777""",
        "document": "fair_housing.md",
        "section": "Fair Housing"
    },

    "how long does maintenance take": {
        "answer": """Maintenance response times at Portico:

EMERGENCY RESPONSE (0-4 hours):
- No heat/AC (seasonal)
- No water supply
- Gas smell
- Electrical hazard
- Roof leak with active dripping
- Broken door/window lock (safety concern)
- Sewage backup

URGENT RESPONSE (1-2 days):
- Appliance malfunction (oven, fridge, washer)
- Plumbing leaks (non-emergency)
- Broken plumbing fixtures
- Sliding door/window malfunction
- Pest infestation

STANDARD RESPONSE (3-7 days):
- Paint touch-ups
- Caulking/weatherstripping
- Door hinges and locks
- Cabinet repairs
- Light fixture replacement
- Flooring damage

TIMELINE COMMUNICATION:
- Estimated completion time provided within 24 hours
- You must grant access at scheduled time (24-hour notice required)
- If you're unable to provide access, you can request another appointment""",
        "document": "maintenance_sop.md",
        "section": "Response Times"
    },

    "what are grounds for eviction": {
        "answer": """Portico enforces lease terms through structured procedures:

NON-PAYMENT OF RENT:
- First violation: Written notice + 3-day cure period
- Second violation: 30-day termination notice
- Eviction filed if payment not made after cure period

LEASE VIOLATIONS:
- First violation: Written warning + 30-day cure period
- Second violation: Non-renewal or 30-day lease termination notice

SERIOUS VIOLATIONS (Immediate action):
- Dangerous pet incidents: Immediate removal required
- Illegal activity on premises
- Violence or threats
- Creating unsafe conditions
- Unauthorized occupants

PROPERTY DAMAGE:
- Intentional damage = Non-renewal + damage charges
- Resident liable for repair costs
- Documentation and photos required for assessment

LEASE TERMINATION NOTICE:
- 30 days' written notice required (except dangerous situations)
- Notice specifies violation and reason for termination
- Resident has right to cure if allowed under lease

For lease violations, always contact property management immediately.""",
        "document": "eviction_procedures.md",
        "section": "Eviction Procedures"
    },

    "can i break my lease early": {
        "answer": """Early lease termination at Portico follows specific procedures:

STANDARD EARLY TERMINATION:
- Requires written request to property manager
- 60-day advance notice minimum (per lease terms)
- Early termination fee applies (typically 1-2 months' rent)
- Final walkthrough scheduled before move-out date

LEASE BREAK EXCEPTIONS (No penalty):
- Job relocation (employer letter required)
- Active military deployment (military orders required)
- Uninhabitable conditions (verified by management)
- Domestic violence situation (documentation required)
- Health emergency (medical documentation)

PROCESS:
1. Submit written request to property manager
2. Provide 60-day advance notice
3. Include reason for early termination
4. Attend final walkthrough
5. Return all keys and access devices
6. Provide forwarding address for security deposit return

LEASE RENEWAL:
- Early renewal discounts may apply
- Lease extension options reviewed 90 days before expiration
- Renewal rates based on market conditions

NOTE: Lease terms vary by location and lease agreement. Always review your specific lease for exact requirements. Contact property management for individual circumstances.""",
        "document": "lease_exceptions.md",
        "section": "Early Termination"
    },

    "what accessibility requirements do properties have": {
        "answer": """Portico properties comply with ADA (Americans with Disabilities Act) accessibility requirements:

COMMON AREA ACCESSIBILITY:
- Accessible parking spaces (designated, near entrances)
- Ramps or elevators for building access
- Wide hallways and doorways (36+ inches minimum)
- Accessible community facilities (leasing office, fitness center, pool)
- Accessible entrances and exits with appropriate signage

UNIT-LEVEL ACCESSIBILITY:
- Accessible bathrooms with grab bars
- Roll-in showers (in designated accessible units)
- Wheelchair-accessible layouts in certain units
- Lower light switches and thermostats
- Accessible kitchen counters and appliances

SERVICE ANIMALS:
- Allowed without pet fees or breed restrictions
- Certification required
- Not classified as "pets" under housing rules
- Common area access permitted

REASONABLE ACCOMMODATIONS:
- Request process: Submit written request to property management
- Response time: 10 business days for determination
- Examples: accessible parking, appliance modifications, accessible entrances
- No additional charges for reasonable accommodations

COMMUNICATION ACCESSIBILITY:
- TTY/TDD devices available
- Communication aids for residents with hearing/speech disabilities
- Documents available in alternative formats upon request

For accessibility concerns or requests: Contact property management or HUD.""",
        "document": "accessibility_requirements.md",
        "section": "Accessibility"
    },

    "are there any lease exceptions": {
        "answer": """Portico offers lease exceptions and modifications in specific situations:

EARLY TERMINATION EXCEPTIONS:
- Job relocation (employer verification required)
- Active military deployment (military orders required)
- Uninhabitable unit conditions (management verified)
- Domestic violence situation (with documentation)
- Serious health emergency (medical documentation)

LEASE MODIFICATION EXCEPTIONS:
- Disability-related modifications (ADA reasonable accommodation)
- Service animal exceptions (no pet fees, no breed restrictions)
- Emotional support animals (requires licensed provider documentation, fees apply)
- Rent assistance programs (income-based, government assistance eligible)
- Extended leases for seniors or disabled residents

RENEWAL EXCEPTIONS:
- Early renewal discounts available 90+ days before expiration
- Month-to-month lease conversions in specific circumstances
- Lease extension with rate lock for excellent residents

OCCUPANCY EXCEPTIONS:
- Additional occupants by written request (subject to lease limits)
- Temporary occupants (guests, visiting family) - see lease terms
- Caregiver exceptions for elderly or disabled residents

PROCESS FOR REQUESTING EXCEPTIONS:
1. Submit written request to property manager
2. Include supporting documentation
3. Allow 10 business days for review
4. Management may request additional information
5. Approval/denial provided in writing with explanation

Each request evaluated individually based on:
- Lease terms
- Company policy
- Circumstances
- Legal compliance

Contact property management for your specific situation.""",
        "document": "lease_exceptions.md",
        "section": "Lease Exceptions"
    },

    "what happens if i'm late on rent": {
        "answer": """Portico's late rent policy protects both residents and the company:

LATE PAYMENT PROCEDURES:
- Rent due: First day of month
- Late fee: Applied if payment not received by 5th of month
- Late fee amount: $50-100 depending on lease (check your lease)
- Grace period: 5 days before late fee applies

PAYMENT OPTIONS:
- Online portal (recommended, no fee)
- Automatic bank draft (no fee)
- Check or money order (mail or drop box)
- In-person at leasing office
- Phone payment (may have processing fee)

LATE PAYMENT CONSEQUENCES:
- First violation: Written notice + 3-day cure period
- Pay late fees to avoid further action
- Pay rent in full during cure period
- Second violation: 30-day lease termination notice
- Eviction proceedings if payment not made after 3-day notice

COMMUNICATION:
- Contact property manager IMMEDIATELY if unable to pay on time
- Payment plans or assistance programs may be available
- Late payment can affect future rental references

FINANCIAL HARDSHIP:
- Discuss situations with property management early
- Emergency assistance programs may apply
- Government rent assistance may be available in your area
- 211.org can help find local resources

PREVENTION TIPS:
- Set up automatic payments
- Contact management at first sign of hardship
- Maintain emergency fund for rent
- Know your payment due date and late fee amount

Note: Failure to pay rent is grounds for eviction. Always pay promptly or communicate with management.""",
        "document": "lease_exceptions.md",
        "section": "Late Payment"
    },

    "how do i renew my lease": {
        "answer": """Portico lease renewal process:

RENEWAL TIMELINE:
- Renewal notice: Provided 90+ days before lease expiration
- Decision deadline: 60 days before lease expiration
- Accept/decline decision required by that date
- Early renewal discounts may apply for advance commitment

RENEWAL OPTIONS:
- 1-year lease renewal (standard)
- 2-year lease renewal (may include discount)
- Month-to-month conversion (in specific situations)
- Lease extension at new terms

RENEWAL RATES:
- Based on current market conditions
- Early renewal may include rate lock discount
- Excellent residents may receive preference pricing
- Rate increases typical annually (2-5% range)

RENEWAL PROCESS:
1. Receive renewal notice 90 days before expiration
2. Review renewal terms and new rent amount
3. Confirm early or wait for final renewal notice (60 days before expiration)
4. Sign renewal lease at leasing office
5. Return signed lease by deadline
6. Continue occupancy on new terms

EARLY RENEWAL BENEFITS:
- Rate lock (guaranteed rate for next 2 years)
- Discount incentive (up to 5% off market rate)
- Payment of next deposit waived
- Lease priority (keep desired unit)

IF NOT RENEWING:
- Provide 60-day notice to vacate
- Schedule final walkthrough
- Coordinate move-out inspection
- Forward mail address for security deposit return

QUESTIONS? Contact property management 90+ days before expiration.""",
        "document": "renewal_procedures.md",
        "section": "Renewal Procedures"
    },
}

# Helper function to find matching answer
def get_static_answer(question: str) -> dict:
    """Find answer for question from static mapping."""
    question_lower = question.lower().strip()

    # Exact match
    if question_lower in STATIC_QA_MAPPING:
        data = STATIC_QA_MAPPING[question_lower]
        return {
            "answer": data["answer"],
            "document": data["document"],
            "section": data["section"],
            "source": "static_qa"
        }

    # Partial match (check if question contains key phrases)
    for key in STATIC_QA_MAPPING.keys():
        if key in question_lower or question_lower in key:
            data = STATIC_QA_MAPPING[key]
            return {
                "answer": data["answer"],
                "document": data["document"],
                "section": data["section"],
                "source": "static_qa"
            }

    return None
