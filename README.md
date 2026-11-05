<div align="center">

# 🧪 web-e2e-behave-selenium

**Automação de Testes Web E2E** &nbsp;·&nbsp; Python &nbsp;·&nbsp; Behave (BDD) &nbsp;·&nbsp; Selenium &nbsp;·&nbsp; Page Object Model

[![E2E Tests](https://github.com/MateusCerqueiraG/web-e2e-behave-selenium/actions/workflows/e2e.yml/badge.svg)](https://github.com/MateusCerqueiraG/web-e2e-behave-selenium/actions/workflows/e2e.yml)
&nbsp;
[![Relatório Allure](https://img.shields.io/badge/📊_Relatório-Allure_ao_vivo-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/web-e2e-behave-selenium/)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4-43B02A?logo=selenium&logoColor=white)
![Behave](https://img.shields.io/badge/BDD-Behave-0A7BFF?logo=cucumber&logoColor=white)
![Chrome](https://img.shields.io/badge/Chrome-✓-4285F4?logo=googlechrome&logoColor=white)
![Firefox](https://img.shields.io/badge/Firefox-✓-FF7139?logo=firefox&logoColor=white)

</div>

---

Suíte de testes **end-to-end** que exercita uma loja real no navegador — login, carrinho e compra — escrita em **Gherkin**, com **Page Object Model**, rodando **cross-browser** e em **CI** a cada push, com relatório **Allure** publicado.

> 🎯 **Alvo sob teste:** [SauceDemo](https://www.saucedemo.com) — app de e-commerce **público, feito para prática de QA**. Nenhum sistema real ou privado é tocado.

## ✅ O que a suíte cobre

| Módulo | Cenários testados |
|:--|:--|
| 🔐 **Login** | login válido · usuário bloqueado · senha obrigatória |
| 🛒 **Carrinho** | adicionar item (badge) · remover item (carrinho vazio) |
| 💳 **Checkout** | compra ponta a ponta · dados obrigatórios (negativo) |

<div align="center">

**7 cenários &nbsp;·&nbsp; 29 passos &nbsp;·&nbsp; Chrome + Firefox &nbsp;·&nbsp; 100% verde**

</div>

## 🧰 Stack & práticas

- 🥒 **BDD** — cenários legíveis em Gherkin (`.feature`)
- 🧩 **Page Object Model** — `BasePage` + 5 páginas, esperas explícitas, separado dos steps
- 🌐 **Cross-browser** — `BROWSER=chrome|firefox`, headless no CI
- 📸 **Evidência** — screenshot anexado ao Allure quando um passo falha
- 🔁 **Anti-flaky** — rerun automático dos cenários que falham + re-clique robusto em forms SPA
- ⚙️ **CI** — GitHub Actions com matriz Chrome + Firefox a cada push

## 📁 Estrutura

```
features/
├── environment.py          # ciclo de vida do driver, cross-browser, screenshot on-fail
├── *.feature               # login · cart · checkout
├── pages/                  # Page Object Model (BasePage + 5 páginas)
└── steps/                  # implementação dos passos Gherkin
.github/workflows/e2e.yml   # CI matriz Chrome + Firefox + publicação do Allure
```

## ▶️ Como rodar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

behave                     # Chrome, headless (padrão)
BROWSER=firefox behave     # Firefox
HEADLESS=false behave      # abre o navegador pra ver
```
> Selenium 4 gerencia os drivers sozinho (Selenium Manager) — sem baixar chromedriver/geckodriver.

## 📊 Relatório Allure

Publicado automaticamente a cada push na `main`:

### 👉 **[mateuscerqueirag.github.io/web-e2e-behave-selenium](https://mateuscerqueirag.github.io/web-e2e-behave-selenium/)**

Localmente:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

---

<div align="center">
<sub>Projeto de portfólio · foco em automação Web E2E com BDD · alvo exclusivamente o app público SauceDemo</sub>
</div>
