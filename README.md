# Overview

Basic self paced computer based training course for learning how to configure and test a Web Application Firewall

# Workstation Setup

You'll need to setup your workstation before proceeding to the main courses.

Start [here](workstation-setup/README.md)

# AEM Dispatcher and Mod_Security

In this course we will use a WAF engine called mod_security that allows us to take an Apache httpd server and give it WAF capabilities but lack of scale (AKA Poor mans WAF).  It's a good starting point to learn the constructs and concepts of a WAF configuration and testing.  In an AEM stack you'll find the AEM Dispatcher typically installed on an Apache httpd webserver.  It's the perfect place to install mod_security and apply advanced blocking rules etc.

[Course 1](mod_security/README.md)