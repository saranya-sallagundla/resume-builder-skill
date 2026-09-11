# Examples — what "good" looks like

Use these as patterns, never as content. Every example below is illustrative; real numbers must come from the candidate.

---

## 1. Bullet transformations (XYZ: result + metric + how)

| Weak | Strong |
|---|---|
| Responsible for handling incidents in the data center. | Resolved 400+ P1–P3 incidents/month across 3 data centers at 99.6% SLA compliance by owning the escalation matrix end to end. |
| Helped with monthly reporting to management. | Cut month-end reporting from 5 days to 2 by automating 14 Excel workbooks into one Power BI model used by 6 department heads. |
| Worked on cloud migration project. | Migrated 42 on-prem workloads to AWS in 7 months with zero unplanned downtime, retiring 3 racks and saving ~$180K/year in colocation cost. |
| Managed a team. | Led a 9-person L2 support team across two shifts; reduced attrition from 30% to 8% in 18 months through structured skill-path and on-call rotation redesign. |
| Involved in testing of application modules. | Designed and executed 320 regression test cases for the claims module, catching 27 pre-release defects and cutting production incidents 35% in the next quarter. |
| Handled customer queries. | Closed 60+ customer tickets/day with 94% first-contact resolution, top 3 of 40 agents for CSAT three quarters running. |
| Good communication skills. | *(Delete. Prove it in a bullet instead:)* Presented weekly RCA summaries to client VP and CIO, turning a red account green within two quarters. |

**Pattern:** number or outcome first → what you did → scope or business effect. One idea per bullet, ≤ 2 lines.

---

## 2. Headlines

| Candidate type | Headline |
|---|---|
| Fresher | Junior Data Analyst \| B.Tech CSE 2025 \| SQL, Python, Power BI |
| Switcher | Cloud Support Engineer \| 6 Yrs Production Operations & Incident Management \| AWS, Linux, Terraform |
| Experienced IC | Senior Mainframe Technical Lead \| 14+ Years \| z/OS, COBOL, DB2, JCL \| ITIL v4 |
| Leadership | Head of Infrastructure Operations \| 15+ Years \| 40-person team, $6M budget \| ITIL, PMP |
| Non-tech | Senior Accountant \| 8 Years \| IFRS, SAP FICO, Month-End Close \| CPA |

---

## 3. Summaries

**Generic (reject):**
> Results-driven professional with a proven track record of leveraging cutting-edge technologies to deliver seamless solutions. Passionate team player seeking a challenging role.

**Specific (accept):**
> Senior mainframe lead with 14 years across banking and healthcare payer systems, currently owning 120+ nightly batch jobs for a US insurer with 99.8% on-time completion. Led two z/OS 2.4→2.5 upgrades and a DB2 v11→v12 migration with no client-facing incidents. Known for RCA depth — reduced repeat incidents 40% in 2023 by fixing root causes the vendor had marked "as designed."

Why the second works: numbers in every sentence, a named technical event, one detail (the vendor "as designed" line) that only this person would write.

**Switcher bridge line:**
> Six years running 24×7 production support for enterprise clients; now applying the same incident, SLA, and automation discipline to cloud infrastructure, with hands-on AWS deployments and Terraform-managed environments.

**Fresher summary:**
> Computer science graduate targeting data analyst roles. Built a retail sales dashboard on 1.2M rows (SQL + Power BI) that identified a 9% margin leak in one product line during a university–industry project. Comfortable moving from raw CSVs to executive-ready visuals; SQL and Python daily.

---

## 4. Key Projects section (credibility builder in practice)

Placed directly after the most recent role. Same formatting as Work Experience. No apologetic language.

```text
KEY PROJECTS
Kubernetes Production Simulation — 2025
• Deployed a 3-service Java application on a 2-node Kubernetes cluster with Prometheus/Grafana monitoring and HPA autoscaling.
• Diagnosed and fixed a recurring ClosedChannelException by aligning connection-pool idle timeout with the ingress keep-alive window; documented the RCA.
• Reduced container image size 60% with multi-stage Docker builds, cutting deploy time from 4 min to 90 sec.
```

Truthful because it happened; confident because it's written like work; safe because it's not under an employer's name.

**Wrong version (misattribution):** the same bullets placed under "ABC Corp — Systems Engineer" when ABC Corp never used Kubernetes. Do not do this.

---

## 5. AI-sounding vs human

| AI-sounding | Human |
|---|---|
| Spearheaded cross-functional initiatives to drive operational excellence. | Ran the weekly change board for 5 application teams; blocked 11 risky Friday deployments in a year, none of which later needed rollback. |
| Leveraged cutting-edge tools to seamlessly optimise workflows. | Replaced a 40-step manual patching checklist with an Ansible playbook; the team now patches 200 servers in one night instead of three. |
| Passionate about delivering exceptional results in dynamic environments. | *(Delete. Passion is shown by the bullets, not claimed.)* |

Signals of human writing: concrete nouns, specific tools with versions, odd real numbers (11, 27, 94%) rather than round ones, a small story inside the bullet, varied sentence length.

---

## 6. Skills section layout

```text
SKILLS
Platforms & OS: IBM z/OS 2.5, Linux (RHEL 8), Windows Server 2019
Languages: COBOL, JCL, REXX, Python (scripting)
Databases: DB2 for z/OS v12, IMS DB, SQL
ITSM & Monitoring: ServiceNow, BMC Remedy, Splunk, CA OPS/MVS
Methodologies: ITIL v4, Incident Management, Change Advisory Board (CAB), Root Cause Analysis (RCA), Agile/Scrum
```

Grouped, plain text, JD terms verbatim, acronyms expanded once.

---

## 7. Defend-your-resume note (one entry)

> **Bullet:** "Reduced repeat incidents 40% in 2023."
> **Likely question:** How did you measure that, and what were the top causes?
> **Answer frame:** Baseline (repeat-incident count Jan–Jun vs Jul–Dec), the three root causes fixed, one example where the vendor pushed back, what you'd do differently.
