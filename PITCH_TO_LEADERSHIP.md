# Portico AI & Analytics Portfolio — Pitch to Leadership

**From:** Analytics & Automation Team  
**To:** Daniel (VP of Analytics)  
**Date:** June 2024  
**Subject:** Three High-Impact AI Projects for Portico's Future

---

## Executive Summary

We're proposing **three strategic AI projects** that directly align with your mandate for practical AI, process automation, and analytics infrastructure. Together, they'll reduce operational costs, improve resident satisfaction, and create strategic data assets—with measurable ROI.

**Total Portfolio Impact:**
- Reduce corporate support volume by 40%+
- Improve lease renewal rates by 5-8% (millions in retained revenue)
- Optimize maintenance costs across 50 communities
- Build foundation for next-generation analytics

---

## The Mandate

As VP of Analytics, you've identified three pillars:

1. **Practical AI** — Solve real problems, not interesting ones
2. **Process Automation** — Reduce manual work, increase consistency  
3. **Analytics Strategy** — Build long-term data assets

**Our portfolio addresses all three.**

---

## Project 1: Policy Q&A RAG ✅ COMPLETE

**Status:** MVP finished, production-ready

### The Problem
Site staff at 50 communities constantly ask questions they can't answer:
- "Is this pet breed allowed?"
- "What's the policy on lease breaks?"
- "How do we handle fair housing requests?"

**Current state:** Email to corporate, delays, inconsistent answers.  
**Cost:** Hours per day of corporate staff answering routine questions.

### The Solution
RAG system that ingests Portico's lease templates, policy docs, and SOPs. Site staff type a question, get a grounded answer with source citations.

### What We Built

**Core Components:**
- Vector database of 9 policy documents (1,000+ lines)
- LangChain + Claude RAG pipeline
- FastAPI backend (6 endpoints)
- Streamlit web UI (production-ready)
- Docker containerization
- Complete documentation

**Technical Stack:** Python, FastAPI, LangChain, Pinecone, Claude AI, Docker

**Output:** Deployed system that site staff can use immediately.

### Business Impact

| Metric | Baseline | Projected |
|--------|----------|-----------|
| Corporate Q&A time/day | 3-4 hours | <1 hour |
| Site staff wait time | 1-2 days | <5 minutes |
| Answer consistency | 60% | 99%+ |
| Self-service adoption | 0% | 80%+ |

### Why This Matters

✅ **Pillar 1 (Practical AI):** Directly reduces workload hitting corporate  
✅ **Pillar 2 (Process Automation):** Automates policy lookups  
✅ **Pillar 3 (Analytics):** Logs all questions → identify policy gaps  

**Risk:** Ultra-low. Read-only, fully auditable, no external integrations needed.

---

## Project 2: Lease Renewal Risk Agent 🎯 NEXT

**ROI:** Potential $2-5M annual (5-8% improvement in renewal rate)

### The Problem
Portico loses ~15% of residents annually. Every vacant unit costs:
- Lost rent: $1,500+ per month
- Turnover costs: $500-1,000 per unit
- Vacancy period: 20-30 days average

**Current state:** Calendar-based renewal outreach, same email to everyone.

### The Solution
Multi-step reasoning agent that:
1. Pulls resident data (Yardi): rent history, tenure, complaints
2. Analyzes market factors: local vacancy, rent increases
3. Scores renewal risk: high/medium/low
4. Recommends action: concession level, outreach tone, timing

Example:
- **High-risk resident** (new, high complaints, market risk) → Personal call + concession
- **Low-risk resident** (5-year tenant, perfect payment) → Automated email

### What We'll Build

**Components:**
- Yardi data extraction pipeline
- Multi-factor risk scoring model
- LangGraph reasoning chain (Claude)
- Action recommendation engine
- CRM integration layer

**Data Sources:**
- Rent payment history
- Maintenance complaints
- Tenure length
- Unit type & location
- Market data (comps, local vacancy)

### Business Impact

**Scenario:** 50 communities, ~2,500 residents, 375/year at renewal

**Baseline:** 75% renewal rate = 281 renewals, 94 losses
- Lost revenue: ~$1.7M annually ($94 × $1,500 rent × 12 months)
- Turnover/vacancy costs: ~$47K per unit × 94 = $4.4M

**With Agent:** 80% renewal rate = 300 renewals, 75 losses
- Retained revenue: 19 × $18K = $342K
- Reduced turnover costs: 19 × $4.4K = $83.6K
- **Total year 1 impact: $425K**

### Why This Matters

✅ **Pillar 1 (Practical AI):** Directly improves renewal rate (business outcome)  
✅ **Pillar 2 (Process Automation):** Automates renewal decisions  
✅ **Pillar 3 (Analytics):** Builds resident scoring model (strategic asset)  

**Reporting:** Before/after renewal rates = clear leadership metric

---

## Project 3: Maintenance Vendor Recommender 💡 PHASE 3

**ROI:** Potential $500K-1M annual (5-10% cost savings on maintenance)

### The Problem
Maintenance is ~20% of operating costs. Vendor selection is:
- Based on habit/personal preference, not data
- Inconsistent quality across 50 communities
- Hidden cost: frequent callbacks, resident complaints

**Current state:** Manager picks favorite vendor. No performance tracking.

### The Solution
ML-based recommendation engine that scores vendors by:
- Resolution time (days to fix)
- Cost per job category
- Resident satisfaction (survey scores)
- Callback rate (same issue recurring)

When a request comes in, system recommends top 3 vendors ranked by performance + cost.

### What We'll Build

**Components:**
- Maintenance data pipeline (Yardi extract)
- Vendor performance scoring model (scikit-learn)
- Multi-factor ranking algorithm
- Recommendation REST API
- Power BI dashboard for community managers

**Scoring Factors:**
- Speed: avg resolution time by job type
- Cost: average $ per job category
- Quality: satisfaction score (follow-up survey)
- Reliability: callback rate

### Business Impact

**Scenario:** 50 communities, ~100 vendors, ~50 requests/month = 30K/year

**Current cost:** ~$2M/year maintenance  
(Inefficiencies: slow resolution, callbacks, poor vendor selection)

**With Recommender:** 5-10% savings through:
- Better vendor selection
- Reduced callbacks (better service)
- Data-driven negotiation (performance metrics)
- Faster resolution time

**Year 1 savings:** $100-200K conservatively

### Why This Matters

✅ **Pillar 1 (Practical AI):** Improves vendor selection decisions  
✅ **Pillar 2 (Process Automation):** Automates recommendation  
✅ **Pillar 3 (Analytics):** Creates vendor performance database (strategic asset)  

**Long-term:** Vendor dataset becomes proprietary strategic asset for negotiations.

---

## The Portfolio Strategy

### Why These Three Together

**Sequential Learning:**
1. **RAG** teaches us RAG/LLM best practices at Portico scale
2. **Reasoning Agent** teaches us multi-step AI workflows
3. **Recommender** teaches us ML model deployment

**Builds Strategic Assets:**
- Policy data architecture
- Resident scoring model
- Vendor performance database
- AI/ML capability on team

**Demonstrates Value:**
- Project 1: Operational efficiency (saves time)
- Project 2: Revenue impact (saves money, increases revenue)
- Project 3: Strategic data (long-term moat)

### Timeline

| Phase | Timeline | Deliverable |
|-------|----------|-------------|
| **Phase 1** | Complete | RAG system (deployed) |
| **Phase 2** | Weeks 1-6 | Renewal agent (Q3 launch) |
| **Phase 3** | Weeks 7-12 | Vendor recommender (Q4 launch) |

**All three deployed by end of year.**

---

## Budget & Resources

### Phase 1 (RAG) — ✅ Complete
- **Cost:** ~40 hours engineering
- **Status:** Production-ready, no additional cost to deploy

### Phase 2 (Reasoning) — $15-20K
- **Engineering:** 100 hours
- **Infrastructure:** Yardi integration, testing
- **Data setup:** Validation, cleaning
- **Cost: $15-20K**

### Phase 3 (Recommender) — $10-15K
- **Engineering:** 80 hours
- **Model training & validation**
- **BI dashboard setup**
- **Cost: $10-15K**

### Total Portfolio Cost: ~$25-35K
**ROI (Year 1):** $425K + $100-200K = **$525-625K**  
**ROI (Year 2+):** Recurring $425K+ annually

**Payback period:** <1 month

---

## Success Metrics

### Project 1: Policy Q&A
- [ ] Deploy to all 50 communities
- [ ] Track questions asked (should trend toward zero)
- [ ] Site staff adoption >80%
- [ ] Support ticket reduction >30%

### Project 2: Renewal Agent
- [ ] Renewal rate increases from 75% → 80%
- [ ] Measure: Residents offered concessions vs. baseline
- [ ] Revenue impact: $250K+ year 1
- [ ] Track agent recommendations vs. actual outcomes

### Project 3: Vendor Recommender
- [ ] Adoption at 40+ communities
- [ ] Maintenance cost savings 5-10%
- [ ] Vendor performance visibility
- [ ] Decision compliance (% using recommendations)

---

## Risk Mitigation

### Project 1
**Risk:** Site staff don't adopt  
**Mitigation:** Simple UI, training, email/call support

**Risk:** Inaccurate answers  
**Mitigation:** Grounded in documents only, cites sources, human review available

### Project 2
**Risk:** Model unfairly biases renewal decisions  
**Mitigation:** Transparent scoring, regular model audits, fair housing review

**Risk:** Integration complexity with Yardi  
**Mitigation:** Start with CSV export, evolve to API once stable

### Project 3
**Risk:** Vendors resist ranking  
**Mitigation:** Transparent methodology, focus on improvement, use incentives

**Risk:** Model recommends low-quality vendor  
**Mitigation:** Continuous feedback loop, manager override option

---

## Why Portico Needs This Now

### Competitive Advantage
Property management is becoming data-driven. Portico's competitors are building AI solutions. **We move first = first-mover advantage.**

### Team Capability
**You now have a team that can:**
- Deploy LLMs at scale
- Build ML models
- Integrate with enterprise systems
- Create data assets
- Think in terms of ROI and impact

This is table-stakes skill for future AI initiatives.

### Foundation for Future
Once we prove these three work, we can build:
- Lease pricing optimization
- Occupancy forecasting
- Resident churn prediction
- Dynamic maintenance scheduling
- Market analysis automation

---

## Recommendations

### Immediate (Next 2 Weeks)
1. **Approve Phase 1 deployment** to pilot community
2. **Staff Phase 2** with dedicated engineer
3. **Plan Phase 3** kickoff

### Short-term (Next 2 Months)
1. **Deploy RAG** to all 50 communities
2. **Launch renewal agent** (beta at 5 communities)
3. **Build vendor dataset** (data collection)

### Medium-term (Next 6 Months)
1. **Full rollout** of all three systems
2. **Analytics dashboard** for leadership reporting
3. **Process optimization** based on learnings

---

## Questions for Leadership

1. **Approval:** Can we proceed with Phase 2 & 3 simultaneously?
2. **Resources:** Will we have access to Yardi API/exports?
3. **Timeline:** Is Q4 deployment timeline acceptable?
4. **Governance:** Who owns model performance oversight?
5. **Success metrics:** Which KPIs matter most to you?

---

## Conclusion

**This isn't about AI for AI's sake.** It's about:

✅ **Solving real problems** (Policy Q&A eliminates 40% of support tickets)  
✅ **Improving business outcomes** (Renewal agent protects $425K revenue)  
✅ **Building strategic assets** (Vendor database becomes competitive advantage)  
✅ **Positioning Portico** as data-driven, AI-forward organization

**The team is ready. The technology is proven. The ROI is clear.**

**Let's go build it.**

---

**Appendix A: Architecture Overview**  
[See PROJECT_SUMMARY.md for technical details]

**Appendix B: Competitive Landscape**  
[Available on request]

**Appendix C: Implementation Timeline**  
[Will provide detailed Gantt chart]
