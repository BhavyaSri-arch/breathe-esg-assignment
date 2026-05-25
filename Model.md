# Decision: SAP Integration Format

I chose CSV flat-file SAP exports instead of live OData/BAPI integration because enterprise ESG onboarding commonly begins with exported operational data before deeper ERP integration work begins.

This approach allowed me to focus on ingestion quality, normalization, and auditability within the assignment timeline.