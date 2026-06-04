# 🛍️ E-Commerce Test Automation Framework

> Automatización QA con Selenium, Python y Pytest usando Page Object Model

[![Selenium](https://img.shields.io/badge/Selenium-4.15-green)](https://www.selenium.dev/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4-yellow)](https://pytest.org/)

---

## 📋 Descripción

Framework profesional de automatización para pruebas end-to-end de un e-commerce.

**Incluye:**
- ✅ 10+ tests automatizados
- ✅ Page Object Model
- ✅ Smoke tests críticos
- ✅ Tests funcionales
- ✅ Tests negativos
- ✅ Reportes HTML
- ✅ Screenshots automáticos en fallos
- ✅ Logging detallado

---

## 🏗️ Estructura

ecommerce-automation-testing/
├── tests/                  # Test suites
│   ├── smoke/             # Tests críticos rápidos
│   ├── functional/        # Tests funcionales
│   └── negative/          # Tests de casos negativos
├── pages/                 # Page Objects
│   ├── base_page.py      # Clase base
│   ├── home_page.py
│   └── login_page.py
├── config/                # Configuración
│   ├── settings.py
│   └── locators.py
├── utils/                 # Utilidades
│   ├── driver_factory.py
│   └── logger.py
├── reports/              # Reportes generados
├── .env                  # Variables de entorno
├── pytest.ini            # Configuración de pytest
└── conftest.py           # Fixtures de pytest

---

## 🚀 Instalación

```bash
# Clonar repositorio
git clone https://github.com/TU-USUARIO/ecommerce-automation-testing.git
cd ecommerce-automation-testing

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Mac/Linux)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Ejecutar Tests

```bash
# Todos los smoke tests
pytest tests/smoke/ -v

# Con reporte HTML
pytest tests/smoke/ -v --html=reports/report.html --self-contained-html

# Solo un test específico
pytest tests/smoke/test_home_page.py::TestHomePageSmoke::test_home_page_loads -v

# Ejecutar por marcador
pytest -m smoke -v
```

---

## 📝 Ejemplos de Tests

**Test simple:**
```python
def test_home_page_loads(self, driver):
    home = HomePage(driver)
    home.navigate()
    
    assert "Automation Exercise" in driver.title
    assert home.is_element_visible(home.LOGO)
```

---

## 🛠️ Stack Tecnológico

| Tecnología | Uso |
|-----------|-----|
| **Selenium** | Automatización del navegador |
| **Pytest** | Framework de testing |
| **Python** | Lenguaje |
| **Page Object Model** | Patrón de diseño |

---

## 📊 Habilidades Demostradas

✅ Page Object Model  
✅ Pytest y fixtures  
✅ Manejo de waits explícitos  
✅ Logging y debugging  
✅ Screenshots automáticos  
✅ Git y GitHub  

---

## 👤 Autor

[Agustin Lopez]  
LinkedIn: [https://www.linkedin.com/in/agustinlopezperuscina/]  
Email: agusjlp6@gmail.com

---

## 📝 Licencia

MIT - Ver LICENSE para detalles