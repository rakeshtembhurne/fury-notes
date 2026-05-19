---
created: 2026-04-08
tags:
  - n8n
  - aws
  - ec2
  - docker
  - hosting
  - automation
source: YouTube transcript
---

# The REAL Way to Host n8n for Free — AWS EC2 & Docker Guide

## Key Insights

1. **AWS EC2 Free Tier = True 24/7 Hosting** - AWS offers 750 hours/month free for 12 months—enough to run a virtual machine continuously. Unlike Render or other middleman platforms, AWS doesn't sleep your server due to inactivity.

2. **Avoid "Free" Platforms with Hidden Catch** - Platforms like Render run on top of AWS anyway but add limitations (server sleep on inactivity, resource restrictions). Go direct to AWS for full control and no artificial constraints.

3. **Docker on EC2 = Professional Setup** - Install Docker on your EC2 instance, then run n8n in a container. This gives you all the benefits of containerization (isolation, easy updates, portability) while leveraging AWS's free tier.

4. **No Middleman Markup** - Using platforms built on AWS still costs them money—they pass those constraints to you. Setting up EC2 directly means you get AWS's full resources within the free tier limits.

5. **Step-by-Step Process Is Straightforward** - Create AWS account → Launch EC2 instance → SSH in → Install Docker → Pull n8n image → Run container. The entire process is well-documented and replicable.

---

*Source: [Eric Tech - The REAL Way to Host n8n for Free - AWS EC2 & Docker Guide](https://www.youtube.com/watch?v=GnckYEpY978)*
