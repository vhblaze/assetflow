# AssetFlow

---

# 🇺🇸 English Version

## AssetFlow

AssetFlow is a production-oriented investment management platform designed to simulate a real-world fintech backend architecture.

This project demonstrates how financial systems must be structured to ensure data integrity, auditability, deterministic calculations, and controlled AI integration.

---

## Why This Project Was Built

Financial systems require more than standard CRUD operations. They demand:

- Transactional integrity  
- Traceable financial state transitions  
- Deterministic portfolio calculations  
- Risk monitoring  
- Strict access control  
- Audit logging  
- Service isolation  

AssetFlow was designed with these constraints in mind.

---

## Architecture Overview

The system is divided into two isolated services:

### Core API (Node.js + Prisma + PostgreSQL)

Responsible for:

- JWT authentication  
- Role-Based Access Control (RBAC)  
- Asset and contribution management  
- Portfolio state transitions  
- Daily portfolio snapshots  
- Profitability and risk calculations  
- Audit logging  
- Financial metric aggregation  

The Core API acts as the single source of business logic and data persistence.

### AI Insight Service (Python + FastAPI)

Responsible for:

- Structured portfolio metric analysis  
- AI-powered daily financial insight generation  
- Deterministic JSON responses  
- Stateless processing  

The AI service does not access the database directly.  
All communication occurs via controlled internal HTTP requests.

---

## Financial Modeling Strategy

Instead of recalculating historical performance dynamically, the system stores daily portfolio snapshots.

This ensures:

- Historical accuracy  
- Deterministic reporting  
- Audit-friendly state reconstruction  
- Performance optimization  
- Reduced computational overhead  

Each snapshot represents the portfolio state at a specific point in time.

---

## AI-Assisted Insight Engine

Daily insights are generated using structured metrics such as:

- Portfolio value  
- Daily and weekly returns  
- Rolling volatility  
- Maximum drawdown  
- Asset concentration  
- Contribution consistency  
- User risk profile  

The AI engine transforms quantitative metrics into contextualized analytical feedback without issuing prescriptive investment advice.

Each insight is versioned and stored for traceability.

---

## Security and Data Integrity

AssetFlow includes:

- Password hashing  
- Expiring JWT authentication  
- Role-based authorization  
- Explicit foreign key constraints  
- Unique constraints on daily portfolio states  
- Indexed time-series queries  
- JSONB metadata fields  
- Audit trail persistence  
- Service-to-service isolation  

PostgreSQL acts as the single source of truth.

---

## Technical Objectives

This project was built to demonstrate:

- Fintech backend architecture  
- Financial data modeling strategies  
- Secure authentication patterns  
- Audit-aware system design  
- Microservice communication  
- AI-assisted decision support systems  
- Production-oriented engineering practices  

---

# 🇧🇷 Versão em Português

## AssetFlow

AssetFlow é uma plataforma de gestão de investimentos orientada a produção, projetada para simular a arquitetura de backend de uma fintech real.

O projeto demonstra como sistemas financeiros devem ser estruturados para garantir integridade de dados, rastreabilidade, cálculos determinísticos e integração controlada de IA.

---

## Por que este projeto foi desenvolvido

Sistemas financeiros exigem mais do que operações básicas de CRUD. Eles demandam:

- Integridade transacional  
- Rastreamento de mudanças no estado financeiro  
- Cálculos determinísticos de carteira  
- Monitoramento de risco  
- Controle rigoroso de acesso  
- Registro de auditoria  
- Isolamento entre serviços  

O AssetFlow foi projetado considerando essas exigências.

---

## Visão Geral da Arquitetura

O sistema é dividido em dois serviços isolados:

### API Principal (Node.js + Prisma + PostgreSQL)

Responsável por:

- Autenticação com JWT  
- Controle de acesso baseado em papéis (RBAC)  
- Gestão de ativos e aportes  
- Transições de estado da carteira  
- Geração de snapshots diários  
- Cálculo de rentabilidade e risco  
- Logs de auditoria  
- Agregação de métricas financeiras  

A API Principal atua como fonte única de lógica de negócio e persistência de dados.

### Serviço de Insights com IA (Python + FastAPI)

Responsável por:

- Análise estruturada de métricas da carteira  
- Geração de insights financeiros diários com IA  
- Retorno determinístico em formato JSON  
- Processamento stateless  

O serviço de IA não possui acesso direto ao banco de dados.  
Toda comunicação ocorre por meio de requisições HTTP internas controladas.

---

## Estratégia de Modelagem Financeira

Em vez de recalcular a performance histórica dinamicamente, o sistema armazena snapshots diários da carteira.

Isso garante:

- Precisão histórica  
- Relatórios determinísticos  
- Reconstrução auditável de estado  
- Otimização de performance  
- Redução de custo computacional  

Cada snapshot representa o estado da carteira em uma data específica.

---

## Engine de Insights com IA

Os insights diários são gerados a partir de métricas estruturadas como:

- Valor total da carteira  
- Retorno diário e semanal  
- Volatilidade em janela móvel  
- Máximo drawdown  
- Concentração por ativo  
- Consistência de aportes  
- Perfil de risco do usuário  

A IA transforma métricas quantitativas em feedback analítico contextualizado, sem emitir recomendações prescritivas de investimento.

Cada insight é versionado e armazenado para garantir rastreabilidade.

---

## Segurança e Integridade de Dados

O AssetFlow inclui:

- Hash seguro de senha  
- JWT com expiração  
- Autorização baseada em papéis  
- Restrições explícitas de chave estrangeira  
- Constraints únicas para estados diários  
- Índices para consultas temporais  
- Uso de JSONB para metadados flexíveis  
- Persistência de trilha de auditoria  
- Isolamento entre serviços  

O PostgreSQL atua como fonte única de verdade.

---

## Objetivos Técnicos

Este projeto foi desenvolvido para demonstrar:

- Arquitetura de backend para fintech  
- Estratégias de modelagem de dados financeiros  
- Padrões de autenticação segura  
- Design orientado a auditoria  
- Comunicação entre microserviços  
- Sistemas de suporte à decisão com IA  
- Práticas de engenharia voltadas para produção  
