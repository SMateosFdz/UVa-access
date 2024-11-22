from selenium import webdriver
from selenium.webdriver.common.by import By

# Simple code to access University of Valladolid online campus, using selenium.
# Your browser may warn you that the session is under remote control, is normal

browser = webdriver.Firefox() # Working with Firefox browser

# URL needs to be like that to work properly
browser.get("https://id.uva.es/SAML2/SSOService.php?SAMLRequest=lZLRT8IwEMb%2FlaXv2%2BiYAxsgQYmRRIUw9MEXc3SHNNna2WtR%2F3u3gRETNfGtubvvu6%2B%2F3IigKmsx9W6nV%2FjikVzwVpWaRNcYM2%2B1MECKhIYKSTgp8untjUiinqitcUaakp1I%2FlYAEVqnjGbBfDZmT1nBh7003WZnvQH0gRebBM8TzPobCYO%2BlBxwkOEAsw0LHtBSoxyzxqiRE3mca3KgXVPqJWnIeciHa54KnoiUP7Jg1vxGaXCdaudcTSKOVRH5PURIcZsqifN8kaPdK4lRvatZMP2MeGk0%2BQrtsXu%2FuvkykVDVnvbKOg%2Flpx80EOOWQRJTfXiEIKm1%2FVHAguUR4IXShdLPf7PbHIZIXK%2FXy3C5yNdsMmq3iI6FnfwjXIUOCnDQZhvFpyajw0HcNevns6UplXwProytwP2ejke8q6gi3HajwmuqUaqtwqIhWpbm9dIiOBwzZz2yeHJY%2Bv3wJh8%3D&RelayState=https%3A%2F%2Fcampusvirtual.uva.es%2Fauth%2Fsaml2%2Flogin.php%3Fwants%26idp%3D728c92232de3ee2b9550501a4529466a%26passive%3Doff&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=ezgTJEjubcilN0O4ycdcGI0dP3EwAH8jhMWwO7IkKtOYxODipxZvCT4QqsqkolGGwy%2FKRCOCAvP7lO2K1ZhdQUjbK5csgWsBx7HGYAPa5zmfVTW6hVBB6GN%2FtCCKB%2BQAtesU72e7rAbmH52U17WsGO%2FgpdzQLku641myUrHCj2wG9hBMj7ckKFtcG6nVM7TZbnDVPBXAp2hQ4ke2qqDfVXKNgiDE%2FQpOdMfU2aHY4R28IPmp0rZcGSwabpxjq4eGRwZfOlsMrpVyXILOgEYI0twKeJ8RMT7xSRC8giphGxHHe67U85NQoT36dPYuE4G%2BQ1AGzfViGCwJU8WPt8PDcg%3D%3D")

searchElem = browser.find_element(By.CSS_SELECTOR, "#edit-name")
searchElem.send_keys("") # your identifier

searchElem = browser.find_element(By.CSS_SELECTOR, "#edit-pass")
searchElem.send_keys("") # your password
searchElem.submit()

