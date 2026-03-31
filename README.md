# Homework: Selenium Basics & PyTest

In this homework, you are going to use Selenium. Before starting the homework tasks make sure that you install Selenium in PyCharm according to the guide given below. Create a repository in your GitHub account and maintain all the tasks in that repository. This will contribute in building your portfolio items. 

[Setting up Selenium in PyCharm](https://www.notion.so/Setting-up-Selenium-in-PyCharm-31eaaf3535384bf8a1f2f2708d0dc50f?pvs=21)

---

## Submission Guideline

In your answer book, add a section related to test automation. For coding related tasks, you will add the code or link to GitHub repository.

---

## Task 1 (Web Automation with Selenium)

You are tasked with automating the following actions on a demo e-commerce website:

**URL:** https://www.saucedemo.com/

### Objectives

1. **Login Automation**  
   Automate the login process using provided credentials.

2. **Product Search Verification**  
   Verify the presence of specific product names after login.

---

### Steps

#### 1. Login to the Website

- Navigate to https://www.saucedemo.com/
- Locate and interact with the login form:
  - Username: `standard_user`
  - Password: `secret_sauce`
- Click the **Login** button
- Verify successful login:
  - Check for products page title or elements

---

#### 2. Verify Specific Product

- After logging in:
  - Locate the product:
    **"Sauce Labs Backpack"**
- Assert that the product name is displayed on the page

---

## Task 2 (Parameterization and Fixtures)

Enhance your login script using PyTest features.

### Requirements

- Implement **parameterization**
- Create a **driver fixture**
- Test all usernames available on:
  https://www.saucedemo.com/

---

## Task 3 (Register User)

Write a Selenium script that performs the following actions:

### URL:
https://automationexercise.com/

---

### Steps

1. Launch browser  
2. Navigate to the URL  
3. Verify that home page is visible successfully  
4. Click on **'Signup / Login'** button  
5. Verify **'New User Signup!'** is visible  
6. Enter name and email address  
7. Click **'Signup'** button  
8. Verify that **'ENTER ACCOUNT INFORMATION'** is visible  

---

### Fill Account Information

- Title  
- Name  
- Email  
- Password  
- Date of birth  

---

### Select Checkboxes

- Sign up for newsletter  
- Receive special offers from partners  

---

### Fill Address Details

- First name  
- Last name  
- Company  
- Address  
- Address2  
- Country  
- State  
- City  
- Zipcode  
- Mobile Number  

---

### Final Steps

13. Click **'Create Account'** button  
14. Verify **'ACCOUNT CREATED!'** is visible  
15. Click **'Continue'** button  
16. Verify **'Logged in as username'** is visible  
17. Click **'Delete Account'** button  
18. Verify **'ACCOUNT DELETED!'** is visible and click **'Continue'** button  

---

## Outcome

By completing this homework, you will:

- Learn Selenium basics  
- Use PyTest fixtures  
- Apply parameterized testing  
- Automate real-world web workflows  

---

✨ Happy Testing!
