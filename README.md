
<h1 align="center">subfinder</h1>

<p align="center">
A program to find subdomain of any domain.
</p>

<kbd> <img src = "https://user-images.githubusercontent.com/63346676/233093306-9efb8f9a-d5f5-49d3-8fbc-6943fdf4e99c.jpeg"></kbd>

Following program enumaretes possible list of sub-domains using Securitytrails API

## Register

Register account in [SecurityTrails.com](https://securitytrails.com/)
Activate Account to get the API Key

>**SETUP PROGRAM**

```python3 setup install```

**Setup API KEY:**

>**For Linux/Macos:**
```
export SD_API_KEY="api_key_value"
```
>**For Windows:**
```
setx [SD_API_KEY] "[api_key_value]"
```
>**Usage:**

```subfinder```

```subfinder --help```
```python3
subfinder --domain vulnweb.com --filepath vulnweb_sd.txt
```
