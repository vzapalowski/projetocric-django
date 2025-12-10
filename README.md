# Projeto RotaCRIC – Django

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-Privada-lightgrey)


---

## 📌 Versão do Projeto
**Versão:** 1.1

---

## 🚀 Como rodar o projeto

### 1. Ativar o ambiente virtual
No Windows (PowerShell):

```ps1
.\venv\Scripts\Activate.ps1
```

### 2. Rodar o servidor de desenvolvimento
python manage.py runserver

### 🗄️ Migrações do Banco de Dados

Criar migrações:

```bash
python manage.py makemigrations
```

Aplicar migrações:

```bash
python manage.py migrate
```

---

## 🔐 Configuração de Segurança - Feature Flags

### FEATURE_EMAIL_ENABLED

O sistema possui uma feature flag para controlar funcionalidades que dependem de email configurado (como redefinição de senha).

**Configuração automática:** Se você não definir `FEATURE_EMAIL_ENABLED`, o sistema detectará automaticamente:
- ✅ Habilitado se `EMAIL_HOST_USER` e `EMAIL_HOST_PASSWORD` estiverem configurados
- ❌ Desabilitado caso contrário

**Configuração manual no `.env`:**
```bash
FEATURE_EMAIL_ENABLED=False  # Desabilita reset de senha e notificações por email
```

**Funcionalidades afetadas:**
- Reset de senha por email (`/reset_password/`)
- Link "Esqueceu a senha?" na tela de login