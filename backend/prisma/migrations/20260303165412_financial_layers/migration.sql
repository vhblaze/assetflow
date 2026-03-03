-- CreateEnum
CREATE TYPE "AuditAction" AS ENUM ('CREATE', 'UPDATE', 'DELETE', 'LOGIN', 'LOGOUT', 'GENERATE_INSIGHT');

-- CreateTable
CREATE TABLE "Contribution" (
    "id" TEXT NOT NULL,
    "portfolioId" TEXT NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "amount" DECIMAL(20,2) NOT NULL,
    "note" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Contribution_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "DailyMetric" (
    "id" TEXT NOT NULL,
    "portfolioId" TEXT NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "portfolioValue" DECIMAL(20,2) NOT NULL,
    "dailyReturnPct" DECIMAL(10,4) NOT NULL,
    "weeklyReturnPct" DECIMAL(10,4) NOT NULL,
    "volatility7dPct" DECIMAL(10,4) NOT NULL,
    "maxDrawdown30dPct" DECIMAL(10,4) NOT NULL,
    "concentrationTop1Pct" DECIMAL(10,4) NOT NULL,
    "concentrationTop3Pct" DECIMAL(10,4) NOT NULL,
    "contributionToday" DECIMAL(20,2) NOT NULL,
    "daysSinceLastContribution" INTEGER NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "DailyMetric_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Insight" (
    "id" TEXT NOT NULL,
    "portfolioId" TEXT NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "headline" TEXT NOT NULL,
    "message" TEXT NOT NULL,
    "tags" TEXT[],
    "confidence" DECIMAL(3,2) NOT NULL,
    "disclaimer" TEXT NOT NULL,
    "rawPayload" JSONB,
    "rawResponse" JSONB,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Insight_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "AuditLog" (
    "id" TEXT NOT NULL,
    "userId" TEXT,
    "action" "AuditAction" NOT NULL,
    "entity" TEXT,
    "entityId" TEXT,
    "metadata" JSONB,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "AuditLog_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "Contribution_portfolioId_date_idx" ON "Contribution"("portfolioId", "date");

-- CreateIndex
CREATE INDEX "DailyMetric_portfolioId_date_idx" ON "DailyMetric"("portfolioId", "date");

-- CreateIndex
CREATE UNIQUE INDEX "DailyMetric_portfolioId_date_key" ON "DailyMetric"("portfolioId", "date");

-- CreateIndex
CREATE INDEX "Insight_portfolioId_date_idx" ON "Insight"("portfolioId", "date");

-- CreateIndex
CREATE UNIQUE INDEX "Insight_portfolioId_date_key" ON "Insight"("portfolioId", "date");

-- CreateIndex
CREATE INDEX "AuditLog_userId_createdAt_idx" ON "AuditLog"("userId", "createdAt");

-- AddForeignKey
ALTER TABLE "Contribution" ADD CONSTRAINT "Contribution_portfolioId_fkey" FOREIGN KEY ("portfolioId") REFERENCES "Portfolio"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "DailyMetric" ADD CONSTRAINT "DailyMetric_portfolioId_fkey" FOREIGN KEY ("portfolioId") REFERENCES "Portfolio"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Insight" ADD CONSTRAINT "Insight_portfolioId_fkey" FOREIGN KEY ("portfolioId") REFERENCES "Portfolio"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "AuditLog" ADD CONSTRAINT "AuditLog_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;
