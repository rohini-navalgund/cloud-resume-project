# ☁️ Serverless Web Application with CI/CD on AWS

A production-ready serverless web application deployed on AWS using modern cloud architecture and an automated CI/CD pipeline.

This project demonstrates real-world cloud engineering skills including infrastructure integration, backend automation, and global content delivery.

---

##  Live Demo

🔗 **CloudFront URL:**
https://d1q2xil4wk3pol.cloudfront.net

---

##  Architecture Diagram

![Architecture](architecture.png)

---

##  Project Overview

This project implements a fully serverless visitor tracking web application using AWS managed services.

The application architecture includes:

* Static frontend hosted on Amazon S3
* Global content delivery via CloudFront CDN
* REST API powered by API Gateway
* Backend logic using AWS Lambda
* Persistent storage using DynamoDB
* Automated deployment using GitHub Actions CI/CD

The system is highly scalable, cost-efficient, and requires zero server management.

---

##  Key Features

* ✅ Fully serverless architecture
* ✅ Automated CI/CD deployment pipeline
* ✅ Global CDN delivery with low latency
* ✅ Real-time visitor counter using DynamoDB
* ✅ Secure API integration
* ✅ Infrastructure aligned with AWS best practices
* ✅ Production-style deployment workflow

---

##  Technologies Used

* Amazon S3
* Amazon CloudFront
* API Gateway
* AWS Lambda (Python)
* DynamoDB
* GitHub Actions
* HTML / CSS / JavaScript

---

##  CI/CD Pipeline

The project uses GitHub Actions to automatically deploy frontend changes to AWS.

### Workflow

1. Developer pushes code to GitHub
2. GitHub Actions workflow triggers
3. Files upload to S3 bucket
4. CloudFront cache invalidation occurs
5. Updated application goes live globally

---

##  Learning Outcomes

This project demonstrates practical experience with:

* Serverless application design
* Cloud deployment automation
* Backend integration with managed services
* CDN optimization strategies
* Infrastructure scalability principles
* Real-world cloud project implementation

---

##  Security & Best Practices

* IAM roles with least privilege access
* Managed AWS services for reliability
* No server maintenance required
* Scalable architecture with pay-as-you-go pricing

---

## 👩‍💻 Author

**Rohini Navalgund**
Cloud & DevOps Enthusiast

---

## ⭐ Future Improvements

* Infrastructure as Code (Terraform / CloudFormation)
* Monitoring with CloudWatch dashboards
* Custom domain with HTTPS
* Authentication integration (Cognito)
* Multi-region deployment

---
