# 🧩 API Documentation

This file lists all functions, classes, and methods extracted from the codebase.

---

{% for file, info in scan_results.items() %}

## 📄 File: `{{ file }}`

---

### 🔧 Functions

{% if info.functions %}
{% for func in info.functions %}

#### ➤ **{{ func.name }}({{ func.args | join(", ") }})**

{{ func.docstring if func.docstring else "_No docstring provided_" }}

---

{% endfor %}
{% else %}
_No functions found_
{% endif %}

---

### 🧱 Classes

{% if info.classes %}
{% for cls in info.classes %}

#### 🏷️ Class **{{ cls.name }}**

{{ cls.docstring if cls.docstring else "_No class docstring provided_" }}

##### Methods:

{% if cls.methods %}
{% for m in cls.methods %}

- **{{ m.name }}({{ m.args | join(", ") }})**  
   {{ m.docstring if m.docstring else "_No method docstring_" }}
  {% endfor %}
  {% else %}
  _No methods found_
  {% endif %}

---

{% endfor %}
{% else %}
_No classes found_
{% endif %}

---

{% endfor %}
