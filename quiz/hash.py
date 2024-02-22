def string_hash(s):
    p = 31
    m = 355
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + (ord(c) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

print(string_hash("Eswatini"))
print(string_hash("Lesotho"))
print(string_hash("Botswana"))

african_countries = [
    "Eswatini",
    "Lesotho",
    "Botswana",
    "Namibia",
    "South Africa",
    "Zimbabwe",
    "Zambia",
    "Mozambique",
    "Malawi",
    "Angola",
    "Tanzania",
    "Kenya",
    "Uganda",
    "Rwanda",
    "Burundi",
    "South Sudan",
    "Sudan",
    "Ethiopia",
    "Somalia",
    "Djibouti",
    "Eritrea",
    "Egypt",
    "Libya",
    "Tunisia",
    "Algeria",
    "Morocco",
    "Western Sahara",
    "Mauritania",
    "Senegal",
    "The Gambia",
    "Guinea-Bissau",
    "Guinea",
    "Sierra Leone",
    "Liberia",
    "Ivory Coast",
    "Ghana",
    "Togo",
    "Benin",
    "Nigeria",
    "Cameroon",
    "Equatorial Guinea",
    "Gabon"
]

print(len(african_countries), len(set(african_countries)), len(set(map(string_hash, african_countries))))
print(set(map(string_hash, african_countries)))