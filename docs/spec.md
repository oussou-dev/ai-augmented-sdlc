# Spec : Enterprise Delivery Intelligence Agent

## Problème
Les équipes delivery ont du mal à suivre l'état de leurs tickets, PR, incidents et déploiements de façon consolidée.

## Objectif
Construire un agent qui analyse ces sources et produit un diagnostic ou une recommandation, avec sources citées et validation humaine pour les actions sensibles.

## Périmètre v1
- Ingestion de tickets (GitHub Issues ou CSV simulé)
- Recherche hybride (BM25 + vecteurs) sur tickets et runbooks
- Agent LangGraph : rewriter → grader → analyst → human gate
- Serveur MCP exposant les outils de recherche et de diagnostic
- Observabilité Langfuse
- CI/CD GitHub Actions

## Critères de succès
- L'agent répond en citant au moins une source fiable
- L'agent refuse de répondre si aucune source fiable n'est trouvée
- Toute action sensible passe par une validation humaine
