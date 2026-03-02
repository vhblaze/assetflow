# AssetFlow

Production-oriented investment management platform designed to simulate a real-world fintech backend architecture.

---

# 🇺🇸 English Version

## Overview

**AssetFlow** is a fintech-oriented backend system built to demonstrate production-grade architecture for financial applications.

It focuses on:

- Deterministic financial calculations  
- Auditability and traceability  
- Secure authentication and authorization  
- Risk-aware portfolio modeling  
- Controlled AI integration  
- Service isolation (microservice-ready architecture)

This project reflects how real financial systems are structured for reliability, compliance, and scalability.

---

## Architecture

AssetFlow is composed of two isolated services:

### 1️⃣ Core API  
**Stack:** Node.js + Prisma + PostgreSQL  

Responsible for:

- JWT authentication  
- Role-Based Access Control (RBAC)  
- Asset and contribution management  
- Portfolio state transitions  
- Daily portfolio snapshots  
- Profitability and risk calculations  
- Audit logging  
- Financial metric aggregation  

The Core API acts as the **single source of truth** for business logic and data persistence.

---

### 2️⃣ AI Insight Service  
**Stack:** Python + FastAPI  

Responsible for:

- Structured portfolio metric analysis  
- AI-generated daily financial insights  
- Deterministic JSON responses  
- Stateless processing  

The AI service does **not** access the database directly.  
All communication occurs via controlled internal HTTP requests.

This separation ensures:

- Security  
- Scalability  
- Deterministic financial control  
- Service independence  

---

## Financial Modeling Strategy

Instead of recalculating historical performance dynamically, AssetFlow stores **daily portfolio snapshots**.

Benefits:

- Historical accuracy  
- Deterministic reporting  
- Audit-friendly state reconstruction  
- Reduced computational overhead  
- Improved query performance  

Each snapshot represents the portfolio state at a specific point in time.

---

## AI Insight Engine

The AI service transforms structured financial metrics into contextual analytical feedback.

### Input Metrics

- Portfolio value  
- Daily and weekly returns  
- Rolling volatility  
- Maximum drawdown  
- Asset concentration  
- Contribution consistency  
- User risk profile  

### Compliance Rules

- No buy/sell recommendations  
- No prescriptive language  
- No invented data  
- Observational tone only  
- Strict JSON validation and normalization  

Each insight is versioned and stored for traceability.

---

## Security & Data Integrity

AssetFlow includes:

- Secure password hashing  
- Expiring JWT authentication  
- RBAC authorization  
- Explicit foreign key constraints  
- Unique constraints for daily portfolio states  
- Indexed time-series queries  
- JSONB metadata fields  
- Persistent audit logs  
- Service-to-service isolation  

PostgreSQL acts as the **single source of truth**.

---

## Project Structure


```text
assetflow/
├── backend/              # Node.js Core API
└── ai-services/          # Python AI Insight Service
    ├── app/
    │   ├── main.py
    │   ├── insight/
    │   │   ├── generator.py
    │   │   ├── prompts.py
    │   │   └── validators.py
    │   └── providers/
    │       ├── base.py
    │       └── llama8b.py
    ├── requirements.txt
    └── README.md
```
---

## Running Locally

### AI Insight Service

From inside the `ai-services` directory:

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Swagger documentation:

http://127.0.0.1:8000/docs

---

## Technical Objectives

This project demonstrates:

- Fintech backend architecture  
- Financial data modeling strategies  
- Secure authentication patterns  
- Audit-aware system design  
- Microservice communication  
- AI-assisted decision support systems  
- Production-oriented engineering practices  

---

# 🇧🇷 Versão em Português

## Visão Geral

**AssetFlow** é um sistema backend orientado a fintech, desenvolvido para demonstrar uma arquitetura de produção voltada a aplicações financeiras.

O projeto foca em:

- Cálculos financeiros determinísticos  
- Auditoria e rastreabilidade  
- Autenticação e autorização seguras  
- Modelagem de risco e carteira  
- Integração controlada de IA  
- Isolamento entre serviços (arquitetura pronta para microserviços)

Ele reflete como sistemas financeiros reais são estruturados para garantir confiabilidade, compliance e escalabilidade.

---

## Arquitetura

O AssetFlow é composto por dois serviços isolados:

### 1️⃣ API Principal  
**Stack:** Node.js + Prisma + PostgreSQL  

Responsável por:

- Autenticação JWT  
- Controle de acesso baseado em papéis (RBAC)  
- Gestão de ativos e aportes  
- Transições de estado da carteira  
- Snapshots diários da carteira  
- Cálculo de rentabilidade e risco  
- Logs de auditoria  
- Agregação de métricas financeiras  

A API Principal atua como **fonte única de verdade** da lógica de negócio e persistência de dados.

---

### 2️⃣ Serviço de Insights com IA  
**Stack:** Python + FastAPI  

Responsável por:

- Análise estruturada de métricas da carteira  
- Geração de insights financeiros diários com IA  
- Retorno determinístico em JSON  
- Processamento stateless  

O serviço de IA **não possui acesso direto ao banco de dados**.  
Toda comunicação ocorre via requisições HTTP internas controladas.

Essa separação garante:

- Segurança  
- Escalabilidade  
- Controle determinístico do backend financeiro  
- Independência entre serviços  

---

## Estratégia de Modelagem Financeira

Em vez de recalcular a performance histórica dinamicamente, o AssetFlow armazena **snapshots diários da carteira**.

Isso garante:

- Precisão histórica  
- Relatórios determinísticos  
- Reconstrução auditável de estado  
- Redução de custo computacional  
- Melhor performance em consultas  

Cada snapshot representa o estado exato da carteira em uma data específica.

---

## Engine de Insights com IA

O serviço de IA transforma métricas financeiras estruturadas em feedback analítico contextualizado.

### Métricas de Entrada

- Valor total da carteira  
- Retorno diário e semanal  
- Volatilidade em janela móvel  
- Máximo drawdown  
- Concentração por ativo  
- Consistência de aportes  
- Perfil de risco do usuário  

### Regras de Compliance

- Não recomendar compra ou venda  
- Não usar linguagem prescritiva  
- Não inventar dados  
- Tom observacional  
- Validação e normalização rigorosa do JSON  

Cada insight é versionado e armazenado para garantir rastreabilidade.

---

## Segurança e Integridade de Dados

O AssetFlow inclui:

- Hash seguro de senha  
- JWT com expiração  
- RBAC  
- Constraints explícitas de chave estrangeira  
- Constraints únicas para estados diários  
- Índices para consultas temporais  
- Campos JSONB para metadados  
- Logs persistentes de auditoria  
- Isolamento entre serviços  

O PostgreSQL atua como **fonte única de verdade**.

---

## Objetivos Técnicos

Este projeto foi desenvolvido para demonstrar:

- Arquitetura backend para fintech  
- Estratégias de modelagem financeira  
- Padrões de autenticação segura  
- Design orientado à auditoria  
- Comunicação entre microserviços  
- Sistemas de suporte à decisão com IA  
- Boas práticas voltadas à produção  
