import random
import os
import subprocess
import argparse
import datetime
from typing import Dict, List
 
class CVGenerator:
    def __init__(self):
        # ARCHÉTYPES
        schools_inge_it = ["EPITA", "INSA Lyon", "CentraleSupélec", "Epitech", "Télécom Paris", "Ensimag", "École 42"]
        schools_uni_it = ["Université Paris-Saclay", "Sorbonne Université", "Université Montpellier", "Claude Bernard Lyon 1"]
        schools_iut_it = ["IUT de Paris - Rives de Seine", "IUT d'Orsay", "IUT de Bordeaux", "IUT Informatique de Lyon"]
 
        self.archetypes = {
            "dev_web": {
                "job_titles": ["Développeur Full-Stack Senior", "Ingénieur Logiciel", "Développeur Front-End"],
                "skills": ["Python", "Java", "React", "Node.js", "TypeScript", "Docker", "Git", "PostgreSQL", "MongoDB", "Vue.js", "GraphQL", "Redis", "Agile / Scrum"],
                "companies": ["TechCorp Solutions", "Capgemini", "Sopra Steria", "Criteo", "Leboncoin", "Doctolib", "BlaBlaCar"],
                "schools_inge": schools_inge_it, "schools_uni": schools_uni_it, "schools_iut": schools_iut_it,
                "fields": ["Génie Logiciel", "Développement Web et Mobile", "Systèmes d'Information"],
                "summaries": [
                    "Développeur passionné et expérimenté, spécialisé dans la conception et le déploiement d'architectures logicielles complexes et scalables. Fort d'une solide expertise technique sur des environnements back-end et front-end, je place l'expérience utilisateur, la sécurité des données et la qualité du code au cœur de mes priorités. J'aime concevoir des API robustes et accompagner des développeurs juniors pour les faire monter en compétences sur les bonnes pratiques de l'industrie (Clean Code, TDD).",
                    "Ingénieur logiciel polyvalent possédant une maîtrise approfondie du cycle de développement complet, de l'analyse fonctionnelle des besoins à la mise en production continue (CI/CD). Je suis particulièrement à l'aise dans les environnements agiles et j'excelle dans la résolution de problèmes algorithmiques complexes. J'ai activement participé à la migration d'architectures monolithiques vers des écosystèmes microservices basés sur le cloud, maximisant ainsi les performances globales et la fiabilité de systèmes critiques.",
                    "Développeur Full-Stack passionné par la création d'applications web performantes et accessibles. Je maîtrise l'écosystème JavaScript/TypeScript et j'apporte une attention particulière à l'architecture logicielle. J'aime résoudre des problèmes complexes et optimiser l'expérience utilisateur finale.",
                    "Ingénieur d'étude et développement spécialisé dans les architectures orientées services (SOA). Fort d'une expérience en refonte d'applications legacy, j'assure la transition vers des technologies modernes (React, Node.js) tout en maintenant une haute disponibilité.",
                    "Développeur Back-End avec une forte appétence pour la gestion de bases de données et la conception d'API REST/GraphQL. Rigoureux et adepte de la Clean Architecture, je veille à la maintenabilité et à la couverture de tests de l'ensemble du code.",
                    "Concepteur développeur web agile, habitué à travailler en étroite collaboration avec les équipes Produit (UX/UI). Je transforme des maquettes complexes en interfaces interactives fluides tout en garantissant une intégration backend robuste.",
                    "Ingénieur logiciel orienté cloud-native, développant des solutions web évolutives et sécurisées. J'intègre les pratiques DevOps au quotidien pour assurer des déploiements fréquents et sans interruption de service.",
                    "Développeur Front-End senior, expert en optimisation des performances web (Core Web Vitals). Je construis des interfaces réactives et modulaires, et j'accompagne la montée en compétences des équipes sur les bonnes pratiques d'intégration et d'accessibilité."
                ],
                "actions": [
                    "Refonte intégrale de l'interface utilisateur en utilisant React et TypeScript, ce qui a conduit à une augmentation de 25% de la rétention client.",
                    "Optimisation des requêtes SQL et migration vers PostgreSQL, améliorant les temps de réponse de l'API de manière significative et réduisant la charge serveur de 30%.",
                    "Développement d'une API REST robuste en Node.js capable d'encaisser plus de 10 000 requêtes par seconde lors des pics de charge saisonniers.",
                    "Encadrement technique d'une équipe de 4 développeurs juniors, incluant la réalisation de revues de code rigoureuses et l'animation d'ateliers de conception.",
                    "Mise en place de tests end-to-end automatisés avec Cypress et Jest, faisant passer la couverture de code globale de 45% à plus de 85%.",
                    "Conception et intégration d'une architecture orientée événements avec Apache Kafka pour synchroniser les données entre plusieurs microservices.",
                    "Audit de sécurité du code legacy et correction de plusieurs vulnérabilités critiques (injections SQL, failles XSS) identifiées par les équipes de pentest.",
                    "Intégration de solutions de paiement tierces (Stripe, PayPal) via des webhooks sécurisés et asynchrones pour la plateforme e-commerce principale.",
                    "Réduction de 50% du temps de build de l'application front-end grâce à une migration stratégique de Webpack vers Vite.",
                    "Migration de l'infrastructure d'hébergement vers AWS (EC2, S3, RDS), garantissant une scalabilité automatique lors des forts pics de trafic.",
                    "Création d'une bibliothèque de composants UI réutilisables sous Storybook, accélérant le développement des nouvelles fonctionnalités front-end de 40%.",
                    "Mise en place d'un système de cache distribué avec Redis, diminuant la latence des requêtes API récurrentes de plus de 60%.",
                    "Migration d'une application monolithique Angular vers une architecture micro-frontends avec React, réduisant la dette technique globale.",
                    "Conception et développement d'un système d'authentification centralisé (SSO) basé sur OAuth2 et JSON Web Tokens (JWT).",
                    "Optimisation des performances de rendu côté client avec la mise en place de Server-Side Rendering (SSR) via Next.js.",
                    "Création de scripts de migration de données massives en Python, traitant plus d'un million d'enregistrements sans perte d'intégrité.",
                    "Intégration continue d'outils d'analyse de code (SonarQube) dans le pipeline GitLab CI, réduisant les bugs en production de 20%.",
                    "Refactoring complet de la couche d'accès aux données avec Prisma ORM pour optimiser les requêtes complexes et limiter les appels superflus.",
                    "Mise en place d'un système d'internationalisation (i18n) couvrant 5 langues différentes pour une application SaaS B2B.",
                    "Développement de WebSockets pour permettre la mise à jour en temps réel des tableaux de bord financiers des utilisateurs.",
                    "Automatisation des tests d'interface utilisateur avec Playwright, couvrant 90% des parcours critiques de l'application e-commerce.",
                    "Collaboration avec l'équipe UX pour implémenter un Dark Mode fluide et persistant sur l'ensemble de la plateforme web.",
                    "Résolution de problèmes de fuites de mémoire (memory leaks) sur une application Node.js à fort trafic, stabilisant l'usage RAM des serveurs.",
                    "Configuration d'un CDN (Content Delivery Network) pour diviser par deux le temps de chargement des ressources statiques à l'international."
                ]
            },
            
            "cybersecu": {
                "job_titles": ["Consultant Cybersécurité", "Ingénieur Sécurité SSI", "Analyste SOC", "Pentester / Ethical Hacker"],
                "skills": ["Python", "Bash", "Wireshark", "Metasploit", "Splunk (SIEM)", "EDR / XDR", "Sécurité Cloud (AWS/Azure)", "Cryptographie", "ISO 27001", "Forensic", "Pentest", "DevSecOps"],
                "companies": ["Thales", "Orange Cyberdefense", "Airbus CyberSecurity", "Wavestone", "Sogeti", "Atos", "ANSSI"],
                "schools_inge": ["EPITA", "INSA Lyon", "Télécom Paris", "Ensimag", "ESIEA", "Epitech"],
                "schools_uni": schools_uni_it, "schools_iut": schools_iut_it,
                "fields": ["Cybersécurité", "Sécurité des Systèmes d'Information", "Réseaux et Sécurité"],
                "summaries": [
                    "Ingénieur en cybersécurité passionné par la protection des infrastructures critiques et la traque des menaces avancées (Threat Hunting). Doté d'une solide expertise technique en test d'intrusion et en réponse à incident, je mets un point d'honneur à sensibiliser les équipes de développement aux enjeux du DevSecOps. Mon objectif est de garantir l'intégrité et la confidentialité des données sensibles face aux cyberattaques.",
                    "Expert en Sécurité des Systèmes d'Information avec une forte appétence pour l'analyse des vulnérabilités et la gestion de crises cyber. Opérant régulièrement au sein de centres de supervision de sécurité (SOC), j'ai développé une grande réactivité pour endiguer les compromissions. Rigoureux et curieux, je réalise une veille technologique constante pour anticiper les nouvelles méthodes des attaquants (APT).",
                    "Expert en cybersécurité spécialisé dans la protection des environnements Cloud (AWS/Azure) et l'architecture Zero Trust. J'accompagne les entreprises dans la sécurisation de leur transformation numérique en intégrant la sécurité dès la phase de conception (Security by Design).",
                    "Auditeur technique et consultant en sécurité offensive (Red Team). Passionné par la recherche de vulnérabilités, je simule des attaques sophistiquées pour éprouver les défenses des organisations et proposer des plans de remédiation pragmatiques et adaptés au contexte métier.",
                    "Analyste SOC de niveau 3 avec une forte expertise en réponse à incident (CSIRT) et en analyse de malwares. Je coordonne les investigations numériques lors d'attaques majeures et j'optimise en continu les règles de détection (Use Cases) du SIEM.",
                    "Ingénieur DevSecOps engagé pour le rapprochement entre les équipes de développement et de sécurité. J'automatise les contrôles de sécurité dans les chaînes CI/CD pour garantir des livraisons logicielles rapides et dénuées de failles critiques.",
                    "Spécialiste en gestion des risques et conformité (GRC), expert des frameworks ISO 27001 et NIS2. J'élabore des politiques de sécurité des systèmes d'information (PSSI) et je pilote les audits de certification pour les opérateurs d'importance vitale (OIV).",
                    "Consultant en gestion des identités et des accès (IAM). Je conçois des architectures de contrôle d'accès sécurisées (MFA, PAM) pour protéger les données sensibles contre les menaces internes et les compromissions de comptes privilégiés."
                ],
                "actions": [
                    "Réalisation de plus de 20 tests d'intrusion (pentests) sur des applications web et des infrastructures internes, avec rédaction de rapports d'audit détaillés.",
                    "Analyse en temps réel des alertes de sécurité remontées par le SIEM (Splunk), permettant la détection et le blocage d'attaques par ransomware.",
                    "Implémentation d'une approche DevSecOps en intégrant des outils d'analyse statique et dynamique (SAST/DAST) directement dans les pipelines CI/CD.",
                    "Animation de campagnes de sensibilisation à la cybersécurité (phishing simulé) ayant permis de réduire le taux de clics dangereux de 40%.",
                    "Investigation numérique (Forensic) suite à une compromission de serveur, identification de la porte dérobée (backdoor) et restauration de l'intégrité du système.",
                    "Déploiement et configuration avancée d'une solution EDR (Endpoint Detection and Response) sur un parc de plus de 5 000 postes de travail.",
                    "Accompagnement à la mise en conformité ISO 27001, incluant la rédaction des politiques de sécurité (PSSI) et la cartographie des risques.",
                    "Conception d'architectures réseaux sécurisées (Zero Trust) pour les environnements Cloud AWS, avec restriction drastique des privilèges IAM.",
                    "Création de scripts d'automatisation en Python pour accélérer la collecte d'artefacts malveillants et l'analyse de logs réseau.",
                    "Gestion des incidents de sécurité de criticité majeure (P1) en coordination avec l'équipe de réponse à incident (CERT) et le comité de direction.",
                    "Reverse engineering de souches virales inédites pour extraire les indicateurs de compromission (IOC) et mettre à jour les bases de signatures.",
                    "Audit de configuration des équipements de sécurité (firewalls, proxys, WAF) pour s'assurer du strict respect des recommandations de l'ANSSI.",
                    "Déploiement d'une solution de gestion des accès à privilèges (PAM) CyberArk pour sécuriser les rebonds d'administration système.",
                    "Analyse de code source (SAST) sur un portefeuille de 20 applications critiques pour éradiquer les vulnérabilités de type injection SQL et XSS.",
                    "Création de playbooks automatisés (SOAR) permettant de réduire le temps de traitement des alertes de phishing de 45 minutes à moins de 5 minutes.",
                    "Organisation d'un exercice de gestion de crise cyber (simulation de ransomware) impliquant la direction générale et la direction de la communication.",
                    "Durcissement (hardening) des configurations de serveurs Windows et Linux conformément aux guides de recommandations de l'ANSSI.",
                    "Réalisation de campagnes de Red Teaming avec contournement des solutions EDR/antivirus pour valider la réactivité du centre de supervision.",
                    "Mise en place d'un programme de Bug Bounty privé ayant permis de corriger 15 failles critiques avant leur exploitation malveillante.",
                    "Développement d'outils de Threat Intelligence en Python pour agréger et analyser des milliers d'indicateurs de compromission (IOC) quotidiens.",
                    "Migration des règles de filtrage firewall (Palo Alto, Fortinet) vers une architecture de micro-segmentation réseau pour limiter les mouvements latéraux.",
                    "Audit de sécurité physique de data centers et de sites industriels, incluant le contournement des contrôles d'accès par badge (RFID cloning).",
                    "Accompagnement des équipes métiers dans la classification de leurs données et le déploiement d'une solution de chiffrement de bout en bout.",
                    "Rédaction de fiches réflexes de réponse à incident pour harmoniser l'intervention technique des analystes SOC lors d'alertes nocturnes."
                ]
            },
 
            "data_ia": {
                "job_titles": ["Data Scientist", "Ingénieur Machine Learning", "Architecte Big Data", "Ingénieur IA"],
                "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Pandas", "Scikit-Learn", "SQL", "Spark", "Hadoop", "Databricks"],
                "companies": ["Dataiku", "Hugging Face", "Criteo", "Thales", "Orange Business Services", "Artefact"],
                "schools_inge": schools_inge_it, "schools_uni": schools_uni_it, "schools_iut": schools_iut_it,
                "fields": ["Intelligence Artificielle", "Data Science", "Mathématiques Appliquées"],
                "summaries": [
                    "Expert en Data Science et Intelligence Artificielle, je conçois des modèles prédictifs performants en exploitant des volumes massifs de données (Big Data). Maîtrisant les algorithmes de Machine Learning et de Deep Learning, j'accompagne les entreprises dans l'automatisation de leurs processus métiers et la valorisation de leur patrimoine de données, tout en assurant une mise en production fiable des algorithmes développés.",
                    "Ingénieur IA passionné par le Traitement du Langage Naturel (NLP) et la Computer Vision. J'aide à transformer des données brutes en insights actionnables grâce à des architectures de réseaux de neurones complexes, tout en assurant leur mise en production via des API performantes. Convaincu par l'approche MLOps, je veille au maintien des performances des modèles tout au long de leur cycle de vie.",
                    "Ingénieur Data Engineer spécialisé dans la création de pipelines de données modernes et scalables. Je transforme des architectures historiques complexes en solutions fluides basées sur le cloud, garantissant une qualité et une disponibilité de la donnée irréprochables pour les équipes métiers.",
                    "Chercheur en intelligence artificielle avec une forte expertise en traitement du langage naturel (NLP) et en modèles de langage de grande taille (LLMs). J'optimise et j'affine (fine-tuning) des modèles open-source pour résoudre des problématiques métiers spécifiques avec une grande précision.",
                    "Data Analyst passionné par la traduction de données brutes en stratégies d'entreprise. Expert en visualisation de données (Dataviz) et en modélisation statistique, je conçois des tableaux de bord décisionnels qui permettent d'identifier rapidement des leviers de croissance.",
                    "Ingénieur MLOps dédié à la robustesse et à la fiabilité des systèmes d'intelligence artificielle en production. J'automatise le cycle de vie des modèles, du versioning des datasets jusqu'au monitoring de la dérive des prédictions (data drift) en temps réel.",
                    "Architecte Big Data avec 10 ans d'expérience dans le déploiement d'écosystèmes distribués (Hadoop, Spark, Kafka). Je conçois des plateformes data-centric (Data Mesh, Data Lakehouse) capables d'ingérer et de croiser des pétaoctets de données hétérogènes.",
                    "Data Scientist spécialisé dans la vision par ordinateur (Computer Vision). J'applique les dernières architectures de Deep Learning (CNN, Transformers) pour automatiser l'analyse d'images médicales ou satellitaires, accélérant ainsi la prise de décision opérationnelle."
                ],
                "actions": [
                    "Entraînement et déploiement de modèles de Machine Learning (NLP) ayant permis d'automatiser 60% des tâches manuelles de classification de documents.",
                    "Conception d'un système de recommandation basé sur le Deep Learning, générant une hausse de 15% du chiffre d'affaires sur le segment e-commerce.",
                    "Mise en place d'un pipeline Big Data avec Apache Spark pour traiter et nettoyer plus de 500 To de données par jour en temps réel.",
                    "Analyse exploratoire des données (EDA) et création de dashboards interactifs avec Tableau, permettant au comité de direction de piloter l'activité.",
                    "Déploiement de modèles prédictifs en production via FastAPI et Docker, avec intégration complète d'une boucle de feedback utilisateur.",
                    "Optimisation des hyperparamètres de modèles Random Forest réduisant le taux de faux positifs de 22% dans le système de détection de fraudes.",
                    "Conception d'une architecture MLOps robuste sur AWS SageMaker pour garantir le suivi des performances et le réentraînement automatique des algorithmes.",
                    "Collaboration avec les experts métiers pour définir les KPIs de succès et extraire les features les plus pertinentes des bases de données historiques.",
                    "Création d'un algorithme de clustering non supervisé pour segmenter la base client en 5 catégories distinctes et optimiser les campagnes marketing.",
                    "Conception d'un modèle de prévision de la demande (Time Series) avec Prophet, réduisant les ruptures de stock de 30% sur l'année.",
                    "Industrialisation de l'extraction de données non structurées (OCR) sur des factures PDF via l'intégration d'API de Computer Vision.",
                    "Mise en place d'une architecture de Feature Store centralisée, facilitant la réutilisation des variables entre les différentes équipes Data.",
                    "Conception de pipelines d'ingestion de données (ETL) asynchrones avec Apache Airflow, gérant quotidiennement plus de 5 millions d'événements.",
                    "Fine-tuning d'un modèle LLM open-source (Llama) pour automatiser la génération de résumés de réunions avec une fidélité évaluée à 95%.",
                    "Réalisation de tests A/B statistiques rigoureux pour évaluer l'impact d'un nouvel algorithme de recommandation, validant une hausse de 8% des ventes.",
                    "Mise en œuvre d'une architecture Data Lakehouse sur Databricks permettant de réduire de 40% les coûts de stockage des données analytiques.",
                    "Création d'un système de détection d'anomalies non supervisé (Isolation Forest) pour alerter les équipes de maintenance industrielle des pannes imminentes.",
                    "Développement d'un modèle de Computer Vision (YOLO) pour le comptage de véhicules en temps réel via des flux de caméras de sécurité urbaines.",
                    "Automatisation de la qualité des données (Data Quality) avec la librairie Great Expectations, bloquant l'intégration de données corrompues en aval.",
                    "Construction de tableaux de bord interactifs sur PowerBI consolidant les données ERP, CRM et e-commerce pour le comité exécutif.",
                    "Déploiement d'un Feature Store centralisé avec Feast, permettant aux équipes Data de partager et réutiliser des variables pré-calculées.",
                    "Mise en place de techniques de NLP avancées (NER) pour extraire automatiquement les clauses clés de milliers de contrats juridiques numérisés.",
                    "Optimisation des requêtes SQL sur Snowflake, réduisant le temps d'exécution des rapports financiers mensuels de 3 heures à 15 minutes.",
                    "Suivi de la dérive des modèles en production (Model Drift) via MLflow, déclenchant des pipelines de réentraînement automatique si la précision chute."
                ]
            },
 
            "game_dev": {
                "job_titles": ["Développeur Gameplay", "Programmeur Moteur 3D", "Ingénieur R&D Jeux Vidéo", "Lead Développeur C++"],
                "skills": ["C++", "C#", "Unreal Engine 5", "Unity 3D", "OpenGL", "Vulkan", "Mathématiques 3D", "Optimisation GPU", "Git", "Perforce"],
                "companies": ["Ubisoft", "Arkane Studios", "Quantic Dream", "Asobo Studio", "Dontnod Entertainment"],
                "schools_inge": ["Cnam ENJMIN", "Isart Digital", "Rubika", "EPITA", "Polytech"],
                "schools_uni": ["Université de Montpellier", "Université Paris 8"],
                "schools_iut": ["IUT Bobigny", "IUT Informatique et Imagerie"],
                "fields": ["Développement de Jeux Vidéo", "Programmation 3D", "Informatique Visuelle"],
                "summaries": [
                    "Ingénieur spécialisé dans le développement de jeux vidéo et la programmation 3D. Passionné par l'optimisation des performances en temps réel et l'architecture de moteurs de jeu, je possède une excellente maîtrise du C++ et des outils de l'industrie (Unreal Engine). Mon approche mathématique et ma rigueur me permettent de repousser les limites visuelles et techniques des plateformes modernes.",
                    "Développeur Gameplay polyvalent avec 5 ans d'expérience dans la création d'expériences ludiques immersives. J'aime collaborer étroitement avec les Game Designers et les artistes techniques pour donner vie à des mécaniques de jeu fluides, intuitives et robustes, en m'assurant que l'expérience manette en main soit toujours parfaitement peaufinée.",
                    "Programmeur Réseau spécialisé dans le développement multijoueur temps réel. Je conçois des architectures client-serveur robustes pour garantir une synchronisation parfaite des états de jeu, compenser la latence et prévenir la triche dans des environnements très compétitifs.",
                    "Artiste Technique (Tech Art) évoluant à l'intersection entre la création visuelle et le code. J'optimise les pipelines de production artistique, rédige des shaders complexes et veille à ce que la vision artistique du jeu respecte les contraintes strictes de performance des moteurs temps réel.",
                    "Développeur Moteur (Engine Programmer) passionné par l'architecture logicielle de bas niveau. Je crée et j'optimise des systèmes core (gestion de la mémoire, multi-threading, physique) pour repousser les limites technologiques des consoles de nouvelle génération.",
                    "Programmeur d'Intelligence Artificielle de jeu, expert en systèmes de navigation, comportement et prise de décision (Utility AI, GOAP). Je crée des adversaires virtuels réalistes et imprévisibles qui s'adaptent dynamiquement aux actions des joueurs.",
                    "Programmeur UI/UX spécialisé dans l'intégration d'interfaces utilisateur interactives et performantes pour l'industrie vidéoludique. J'implémente des menus complexes, des HUD diégétiques et je garantis l'accessibilité du jeu pour tous les profils de joueurs.",
                    "Généraliste Game Dev avec un fort profil polyvalent sur Unity. Habitué des équipes indé ou AA, j'interviens aussi bien sur le scripting des outils internes que sur l'intégration des assets audios et la finalisation des builds pour la certification des plateformes."
                ],
                "actions": [
                    "Développement de mécaniques de gameplay en C++ et optimisation du rendu graphique sur Unreal Engine pour un titre AAA, garantissant 60 FPS constants.",
                    "Création d'un système d'intelligence artificielle (Behavior Trees) pour les PNJ, rendant leurs réactions plus réalistes et adaptatives face au joueur.",
                    "Optimisation de la gestion de la mémoire et réduction du temps de chargement des niveaux de 40% grâce au streaming asynchrone des assets 3D.",
                    "Implémentation de shaders personnalisés et de systèmes de particules avancés avec Niagara pour améliorer la qualité visuelle globale du jeu.",
                    "Développement d'outils internes pour l'éditeur de niveau, augmentant de 30% la productivité de l'équipe de Level Design au quotidien.",
                    "Intégration d'un moteur physique multi-threadé permettant de simuler des destructions de décors complexes à grande échelle sans perte de framerate.",
                    "Mise en place d'une architecture réseau fiable pour le mode multijoueur (client-serveur avec prédiction côté client et compensation du lag).",
                    "Profilage CPU/GPU intensif à l'aide de PIX et RenderDoc pour identifier et corriger les goulots d'étranglement avant la phase de certification console.",
                    "Refactoring complet du système d'inventaire modulaire, le rendant compatible avec la sauvegarde cloud multi-plateformes.",
                    "Intégration d'outils de télémétrie in-game pour récolter les données de parcours des joueurs et ajuster la difficulté dynamiquement.",
                    "Développement d'un système de cinématiques temps réel, permettant de synchroniser les animations faciales avec le doublage audio.",
                    "Portage complet du moteur de jeu vers les consoles nouvelle génération (PS5, Xbox Series X), en exploitant au maximum les architectures SSD.",
                    "Développement d'un algorithme de Pathfinding A* optimisé sur plusieurs threads, permettant de calculer les itinéraires de 500 unités simultanément.",
                    "Création de shaders volumétriques et de post-processing sous HLSL/GLSL, améliorant significativement l'ambiance lumineuse d'un environnement extérieur.",
                    "Mise en place de Memory Pools et d'allocateurs de mémoire personnalisés pour supprimer totalement les micro-gels (stutters) dus au Garbage Collector.",
                    "Programmation d'un système de matchmaking basé sur la compétence (Elo/Glicko) intégrant une gestion fluide de la reconnexion des joueurs déconnectés.",
                    "Architecture et implémentation d'un système de Machines à États (FSM) pour l'interface utilisateur, rendant la navigation dans les menus 30% plus réactive.",
                    "Intégration et ajustement du moteur physique Havok pour simuler le comportement réaliste de véhicules off-road sur des terrains déformables.",
                    "Développement d'un pipeline d'automatisation d'intégration continue (Jenkins/Perforce) pour générer des builds quotidiens (Nightly) sur PC, PS5 et Xbox.",
                    "Création d'un outil d'édition de quêtes (Quest Editor) in-engine, permettant aux Game Designers de scripter des événements sans écrire une seule ligne de code.",
                    "Implémentation d'un système d'Animation Blending complexe avec l'outil state machine d'Unreal Engine pour des transitions de mouvements ultra-réalistes.",
                    "Optimisation agressive des appels de rendus (Draw Calls) et des niveaux de détails (LOD) permettant au jeu de tourner à 60 FPS sur du matériel mobile.",
                    "Mise au point d'une architecture audio 3D spatialisée avec Wwise, renforçant l'immersion sonore des joueurs en fonction de l'environnement virtuel.",
                    "Résolution de crashs critiques de corruption de la mémoire via l'utilisation poussée de debuggers (Visual Studio, WinDbg) en période de Beta fermée."
                ]
            },
 
            "bio_info": {
                "job_titles": ["Bio-informaticien", "Chercheur en Bio-informatique", "Ingénieur Data Santé", "Analyste Génomique"],
                "skills": ["Python", "R", "BioPython", "Bash", "Analyse Génomique", "NGS", "Bases de données biologiques", "Docker", "Statistiques", "Nextflow"],
                "companies": ["Institut Pasteur", "Sanofi", "Inserm", "Doctolib", "Moderna", "BioMérieux"],
                "schools_inge": ["INSA Toulouse", "Polytech Nice Sophia", "EISTI"],
                "schools_uni": ["Université Paris Cité", "Sorbonne Université", "Université d'Évry"],
                "schools_iut": ["IUT Génie Biologique", "IUT Informatique option Santé"],
                "fields": ["Bio-informatique", "Biologie Moléculaire et Informatique", "Data Science pour la Santé"],
                "summaries": [
                    "Bio-informaticien doté d'une double compétence en biologie et en développement informatique. J'accompagne les équipes de recherche dans le traitement, l'analyse et la visualisation de données génomiques à grande échelle pour accélérer les découvertes médicales. Je maîtrise la mise en place de pipelines reproductibles et le déploiement sur des clusters de calcul haute performance (HPC).",
                    "Ingénieur spécialisé dans le traitement des données de santé. Je conçois des pipelines d'analyse automatisés et robustes pour séquencer l'ADN et identifier des biomarqueurs. Passionné par la recherche biomédicale, j'évolue à l'interface entre la médecine de précision et la data science, tout en respectant strictement les normes de confidentialité des données patients (RGPD, HDS).",
                    "Bio-informaticien spécialisé en génomique clinique et médecine personnalisée. J'analyse les données de séquençage à haut débit (NGS) pour identifier des mutations pathogènes, tout en concevant des outils d'aide à la décision à destination des généticiens médicaux.",
                    "Biostatisticien et analyste de données omiques (transcriptomique, protéomique). J'accompagne les chercheurs en validant la puissance statistique de leurs expérimentations et en réalisant des analyses exploratoires complexes pour extraire le sens biologique des données multi-omiques.",
                    "Ingénieur de recherche en bio-informatique structurale. Je modélise les interactions moléculaires (docking protéine-protéine, dynamique moléculaire) et j'exploite l'apprentissage automatique pour accélérer la découverte et le design in silico de nouvelles molécules thérapeutiques.",
                    "Développeur de pipelines bio-informatiques (Data Engineer pour la biologie). Je conçois des flux d'analyses reproductibles, évolutifs et cloud-ready à l'aide de Snakemake ou Nextflow, optimisant ainsi le traitement massif de données issues de consortiums internationaux.",
                    "Spécialiste en bases de données biologiques et intégration sémantique. Je consolide les connaissances éparses issues d'articles scientifiques et de dépôts publics pour structurer des graphes de connaissances (Knowledge Graphs) utiles à l'IA générative en santé.",
                    "Chercheur en métagénomique environnementale. J'analyse l'ADN issu d'échantillons complexes (microbiomes) pour identifier de nouvelles espèces bactériennes et comprendre leurs interactions écologiques à l'aide d'outils statistiques avancés sous R et Python."
                ],
                "actions": [
                    "Analyse de larges jeux de données de séquençage (NGS) à l'aide de scripts Python et R, aboutissant à l'identification de nouveaux biomarqueurs tumoraux.",
                    "Développement de pipelines bio-informatiques reproductibles avec Nextflow et Docker, réduisant le temps d'analyse des génomes de 3 jours à 12 heures.",
                    "Croisement et intégration de multiples bases de données biologiques publiques (NCBI, Ensembl, ClinVar) pour annoter des variants génétiques rares.",
                    "Rédaction de rapports d'analyse statistique détaillés avec RMarkdown pour orienter les décisions lors des essais cliniques de phase 2 du laboratoire.",
                    "Gestion et optimisation des requêtes sur un cluster de calcul haute performance (HPC) sous Slurm pour le traitement de pétaoctets de données brutes.",
                    "Création d'applications web interactives avec R Shiny permettant aux biologistes d'explorer visuellement les résultats d'expression génique (RNA-Seq).",
                    "Développement d'un algorithme de machine learning capable de prédire l'interaction protéine-ligand avec une précision de 88%.",
                    "Conception d'une base de données relationnelle sécurisée (HDS) centralisant les données phénotypiques et génotypiques d'une cohorte de 10 000 patients.",
                    "Automatisation du nettoyage et du contrôle qualité (QC) des données issues des séquenceurs Illumina, réduisant les erreurs d'alignement de 15%.",
                    "Modélisation structurelle 3D de protéines et simulation de dynamique moléculaire, permettant de valider l'affinité de nouvelles molécules thérapeutiques.",
                    "Conception d'une API RESTful sécurisée pour interroger les bases de données génomiques depuis les applications cliniques partenaires.",
                    "Automatisation des rapports de diagnostic génétique à l'aide de scripts RMarkdown, garantissant une traçabilité totale pour les audits de santé.",
                    "Analyse de données RNA-seq (bulk et single-cell) via des pipelines R/Bioconductor, permettant l'identification de gènes différentiellement exprimés liés à une résistance tumorale.",
                    "Simulation de dynamique moléculaire (GROMACS) et docking in silico (AutoDock) ayant permis de présélectionner 5 molécules candidates pour des tests in vitro.",
                    "Développement d'un pipeline Snakemake pour l'annotation automatique des variants cliniques, divisant par quatre le temps de rendu des résultats diagnostiques.",
                    "Conception de modèles statistiques sous R pour évaluer l'efficacité clinique d'un nouveau traitement à partir des données de vie réelle (Real World Data).",
                    "Création d'une API REST Flask permettant l'interrogation rapide d'une base de données interne répertoriant plus d'un million de mutations somatiques annotées.",
                    "Réalisation d'analyses phylogénétiques et d'alignements de séquences multiples sur un cluster HPC pour retracer l'évolution de souches virales émergentes.",
                    "Nettoyage, normalisation et intégration de cohortes cliniques multi-centriques dans un environnement sécurisé respectant les certifications HDS et RGPD.",
                    "Déploiement d'un portail web interactif (R Shiny/Dash) permettant aux biologistes non codeurs de visualiser et de filtrer par eux-mêmes leurs résultats d'expérimentation.",
                    "Optimisation de l'outil BLAST pour une recherche ultra-rapide d'homologies locales sur une base de données de protéines propriétaire de plusieurs téraoctets.",
                    "Entraînement d'un modèle d'apprentissage automatique (Random Forest) pour prédire l'issue thérapeutique des patients en fonction de leur profil métabolomique.",
                    "Mise en place de conteneurs Docker/Singularity pour garantir la reproductibilité totale des analyses computationnelles publiées dans un article scientifique.",
                    "Analyse fonctionnelle de communautés microbiennes (métagénomique shotgun) pour évaluer l'impact d'un régime alimentaire spécifique sur le microbiote intestinal."
                ]
            },
 
            "devops": {
                "job_titles": ["Ingénieur DevOps", "Architecte Cloud", "Site Reliability Engineer (SRE)", "Ingénieur Système & Réseau"],
                "skills": ["Docker", "Kubernetes", "AWS", "GCP", "Terraform", "Ansible", "GitLab CI/CD", "Linux", "Python", "Bash", "Prometheus", "Grafana"],
                "companies": ["AWS France", "Google Cloud", "OVHcloud", "Datadog", "Orange Business Services", "Capgemini", "ManoMano"],
                "schools_inge": schools_inge_it, "schools_uni": schools_uni_it, "schools_iut": schools_iut_it,
                "fields": ["Cloud Computing", "Réseaux et Sécurité", "Infrastructures et Systèmes"],
                "summaries": [
                    "Ingénieur DevOps et Cloud certifié, expert dans l'automatisation des infrastructures et la mise en place de pipelines CI/CD. J'aide les équipes de développement à livrer plus rapidement et en toute sécurité en adoptant les principes de l'Infrastructure as Code (IaC) et la conteneurisation des applications. Je milite pour la culture DevOps au quotidien.",
                    "Site Reliability Engineer passionné par la haute disponibilité et la performance des systèmes distribués. J'interviens sur la sécurisation, le monitoring et la scalabilité des serveurs cloud pour garantir un taux de disponibilité (SLA) de 99,99% sur les applications critiques. Mon but est de construire des infrastructures capables de résister à n'importe quel incident.",
                    "Architecte Cloud expérimenté (AWS/Azure) avec un focus sur l'Infrastructure-as-Code (IaC) et la résilience systémique. J'accompagne la migration des applications monolithiques vers le cloud en garantissant la sécurité, l'élasticité et l'optimisation financière (FinOps).",
                    "Site Reliability Engineer (SRE) dédié à l'observabilité et à la réduction des temps d'indisponibilité. En m'appuyant sur les Service Level Objectives (SLO) et le monitoring proactif, j'assure l'équilibre parfait entre le déploiement de nouvelles fonctionnalités et la stabilité des services.",
                    "Ingénieur Kubernetes et spécialiste de la conteneurisation. Je conçois, déploie et maintiens des clusters K8s de production à grande échelle. J'automatise le scaling et la sécurité des pods via des Operators et des Service Meshes (Istio, Linkerd).",
                    "Expert en automatisation CI/CD et Release Management. Je conçois des pipelines de livraison logicielle fluides, standardisés et sécurisés qui permettent aux équipes de développeurs de passer du code local à la mise en production en quelques minutes, sans frictions.",
                    "Ingénieur SecOps / DevSecOps engagé dans l'automatisation de la conformité. J'intègre la gestion des secrets, l'analyse d'images Docker et la vérification des vulnérabilités au cœur même de l'infrastructure, assurant une conformité continue sans ralentir l'innovation.",
                    "Spécialiste FinOps et optimisation cloud. J'analyse finement l'utilisation des ressources d'infrastructure, mets en place des stratégies d'extinction hors heures ouvrées et optimise les choix d'instances pour maximiser le retour sur investissement des plateformes cloud."
                ],
                "actions": [
                    "Conception d'une infrastructure cloud résiliente sur AWS via Terraform (IaC), assurant une haute disponibilité des services et une scalabilité horizontale automatique.",
                    "Mise en place de pipelines d'intégration et de déploiement continus (CI/CD) sur GitLab automatisant l'ensemble des tests et le déploiement sur les clusters Kubernetes.",
                    "Implémentation d'un système de monitoring complet avec Prometheus et Grafana, réduisant le temps de détection des pannes (MTTD) de 60%.",
                    "Migration de 50 applications legacy vers une architecture conteneurisée sous Docker, réduisant drastiquement les coûts d'hébergement annuels.",
                    "Automatisation du provisionnement et de la configuration des serveurs Linux à l'aide de playbooks Ansible, éliminant les erreurs manuelles.",
                    "Mise en place d'une stratégie de sauvegarde automatisée (Disaster Recovery Plan) avec des tests de restauration trimestriels réussis à 100%.",
                    "Audit de l'infrastructure cloud and application des principes du FinOps, permettant une réduction de la facture mensuelle AWS de 25%.",
                    "Gestion et sécurisation des secrets de l'entreprise via HashiCorp Vault, avec rotation automatique des clés d'accès des API tierces.",
                    "Astreinte technique (On-call) et résolution d'incidents critiques en production de niveau 3 (N3), avec rédaction de post-mortems détaillés (blameless).",
                    "Déploiement d'une politique de sécurité 'Zero Trust', incluant la gestion stricte des identités (IAM) et le chiffrement des données au repos.",
                    "Mise en place d'une architecture de journalisation centralisée (ELK Stack), facilitant l'analyse des logs et le diagnostic des anomalies en production.",
                    "Organisation de sessions de formation internes (Tech Talks) sur les bonnes pratiques de conteneurisation et l'usage optimal de Git.",
                    "Mise à niveau (upgrade) de clusters Kubernetes en production vers des versions majeures sans aucune interruption de service (Zero Downtime).",
                    "Configuration avancée de Datadog APM pour tracer les requêtes distribuées entre 40 microservices et identifier l'origine des ralentissements applicatifs.",
                    "Industrialisation des modules Terraform et gestion centralisée des états (Terraform State) sur S3 pour uniformiser l'architecture entre les environnements Dev et Prod.",
                    "Optimisation des coûts AWS (FinOps) via l'utilisation d'instances Spot et la réservation de capacité, générant une économie de 120k€ sur l'année.",
                    "Refonte globale des templates GitLab CI/CD pour introduire des tests de sécurité automatisés (Trivy, Sonar) sur chaque Merge Request (Shift-Left Security).",
                    "Exécution d'expériences de Chaos Engineering (Chaos Mesh) en pré-production pour valider le comportement de l'infrastructure face à la perte brutale de nœuds réseau.",
                    "Mise en place d'un système de Service Mesh (Istio) permettant d'acheminer le trafic intelligemment (Canary Releases) et de sécuriser les flux intra-cluster (mTLS).",
                    "Création de playbooks Ansible idempotents pour le provisionnement hybride de parcs de serveurs physiques (Bare Metal) et de machines virtuelles.",
                    "Configuration d'une politique de Disaster Recovery (DRP) inter-régions sur AWS avec des RTO/RPO validés inférieurs à 15 minutes.",
                    "Centralisation et rotation automatisée de plus de 500 secrets d'application (clés API, certificats SSL, mots de passe BDD) via HashiCorp Vault.",
                    "Mise en place d'un système de log unifié (Fluentd / ElasticSearch / Kibana) traitant jusqu'à 30 000 événements de journalisation par seconde.",
                    "Création de tableaux de bord Grafana alertant directement sur Slack/PagerDuty en cas de dépassement critique des seuils d'erreurs HTTP 5xx."
                ]
            },
 
            "btp": {
                "job_titles": ["Conducteur de Travaux Principal", "Chef de Chantier", "Ingénieur BTP", "Directeur de Projet Construction"],
                "skills": ["AutoCAD", "MS Project", "Revit (BIM)", "Gestion budgétaire", "Management d'équipes", "Topographie", "Normes QSE", "Droit de la construction"],
                "companies": ["Vinci Construction", "Bouygues Immobilier", "Eiffage Génie Civil", "Colas", "Spie Batignolles", "NGE"],
                "schools_inge": ["ESTP Paris", "École des Ponts ParisTech", "INSA (Département Génie Civil)", "Polytech Lille", "Centrale Nantes"],
                "schools_uni": ["Université Gustave Eiffel", "Université de Strasbourg", "Université Paul Sabatier"],
                "schools_iut": ["IUT Génie Civil de Lyon", "IUT de Rennes", "Lycée Cantau (BTP)"],
                "fields": ["Génie Civil", "Travaux Publics et Infrastructures", "Bâtiment Gros Œuvre"],
                "summaries": [
                    "Ingénieur BTP et Conducteur de Travaux chevronné, justifiant d'une solide expérience de terrain dans le pilotage global de projets de construction de grande envergure. Mon expertise s'étend sur l'intégralité du cycle de vie d'un projet, de la préparation de chantier jusqu'à la réception finale des ouvrages. Je suis le garant incontesté du strict respect des délais et des normes de sécurité.",
                    "Expert en gestion de chantiers et en direction de travaux, je mets mon savoir-faire au service de projets de construction ambitieux. Ayant évolué au sein de grands groupes du BTP, j'ai acquis une méthodologie rigoureuse dans l'optimisation des modes opératoires et l'allocation des ressources. Habitué à gérer des situations complexes, je garantis une communication transparente avec la maîtrise d'ouvrage.",
                    "Ingénieur travaux publics spécialisé dans les infrastructures de transport et les ouvrages d'art. J'orchestre des chantiers complexes (VRD, terrassement, ponts) en gérant de multiples interfaces, les aléas géotechniques et la coordination des concessionnaires de réseaux fluides.",
                    "Conducteur de travaux en réhabilitation et rénovation lourde de bâtiments historiques. Habitué à intervenir en site occupé et à gérer les découvertes imprévues sur chantier (amiante, renforcements structurels), je veille à préserver le patrimoine tout en le modernisant.",
                    "Chef de projet BIM (Building Information Modeling). Je supervise la modélisation 3D collaborative des maquettes numériques, détecte les conflits (clashs) entre les lots techniques en phase d'études, et garantis l'intégrité des données tout au long du cycle de vie du bâtiment.",
                    "Responsable QSE (Qualité, Sécurité, Environnement) pour les grands projets de construction. Je déploie la politique de prévention des risques de l'entreprise sur le terrain, certifie les pratiques selon les normes ISO, et sensibilise continuellement les équipes aux chantiers 'zéro accident'.",
                    "Ingénieur études de prix et méthodes. J'analyse minutieusement les dossiers de consultation (DCE), chiffre les coûts de construction, propose des variantes techniques optimisées pour remporter les appels d'offres, et rédige les mémoires techniques de l'entreprise.",
                    "Directeur de travaux expérimenté, pilotant l'activité de plusieurs chantiers simultanément. Je suis garant de la rentabilité globale des opérations, du maintien des relations commerciales avec les maîtrises d'ouvrage, et j'encadre une équipe d'ingénieurs et de chefs de chantier."
                ],
                "actions": [
                    "Supervision des équipes d'exécution sur le chantier et gestion des plannings d'intervention, assurant une parfaite synchronisation entre le gros œuvre et le second œuvre.",
                    "Coordination stratégique avec 15 entreprises sous-traitantes et les bureaux d'études techniques pour garantir la conformité architecturale et structurelle du projet.",
                    "Suivi financier rigoureux d'un budget global de plus de 5 millions d'euros, incluant l'optimisation des achats de matériaux et la négociation des avenants.",
                    "Application stricte de la politique Qualité, Sécurité, Environnement (QSE) on site, conduisant à l'obtention de zéro accident de travail avec arrêt.",
                    "Rédaction hebdomadaire des rapports d'avancement de chantier, animation des réunions de pilotage et présentation des indicateurs de performance (KPI).",
                    "Pilotage complet des opérations de levée des réserves lors de la livraison du bâtiment, garantissant l'entière satisfaction du client final.",
                    "Réponse technique aux appels d'offres (chiffrage, métré, proposition de variantes techniques) ayant permis de remporter 3 marchés publics majeurs.",
                    "Implantation topographique sur site et vérification quotidienne du bon respect des plans d'exécution fournis par le bureau d'études béton armé.",
                    "Gestion des démarches administratives complexes (autorisations de voirie, DT/DICT) et maintien de bonnes relations avec les riverains du chantier.",
                    "Conduite des réunions de chantier inter-entreprises hebdomadaires, avec rédaction et diffusion des comptes rendus d'avancement à l'ensemble des parties.",
                    "Supervision des études d'exécution et validation des plans de synthèse, permettant d'anticiper les conflits entre les réseaux CVC, plomberie et électricité.",
                    "Gestion des relations avec les bureaux de contrôle (Apave, Socotec) pour garantir l'obtention des attestations de conformité finale avant la livraison.",
                    "Gestion des approvisionnements et contrôle rigoureux des livraisons de matériaux sur site pour éviter les ruptures de stock.",
                    "Pilotage du déploiement des moyens de levage (grues à tour) et optimisation des rotations quotidiennes.",
                    "Animation des quarts d'heure sécurité hebdomadaires pour sensibiliser les compagnons aux risques spécifiques du chantier.",
                    "Réception des supports et validation minutieuse des ferraillages avec le bureau de contrôle avant chaque coulage de béton.",
                    "Négociation financière des contrats de sous-traitance et rédaction des pièces administratives des marchés.",
                    "Suivi des indicateurs de performance environnementale du chantier, incluant le tri des déchets et le bilan carbone.",
                    "Organisation et adaptation des phasages de travaux en site occupé afin de minimiser les nuisances pour les usagers.",
                    "Mise à jour hebdomadaire des plannings sous MS Project en anticipant les aléas climatiques et logistiques.",
                    "Contrôle de la stricte conformité des ouvrages exécutés par rapport aux plans visés 'Bon Pour Exécution' (BPE).",
                    "Réalisation des métrés contradictoires avec les sous-traitants pour la validation mensuelle des situations de travaux.",
                    "Anticipation des besoins en main-d'œuvre, gestion de l'intérim et suivi du pointage des équipes propres.",
                    "Élaboration et mise à jour des Plans Particuliers de Sécurité et de Protection de la Santé (PPSPS) en accord avec le coordonnateur SPS."
                ]
            },
            
            "marketing": {
                "job_titles": ["Responsable Marketing Digital", "Chef de Produit Senior", "Growth Hacker", "Responsable Communication"],
                "skills": ["SEO", "SEA (Google Ads)", "Google Analytics", "Social Media Management", "Content Strategy", "Email Marketing", "Copywriting", "CRM (HubSpot)", "Market Analysis", "Brand Management"],
                "companies": ["Publicis Sapient", "Havas Media", "L'Oréal", "LVMH", "Veepee", "ManoMano", "Agences 360"],
                "schools_inge": ["HEC Paris", "ESSEC Business School", "EDHEC"],
                "schools_uni": ["CELSA", "IAE Paris", "Sorbonne - Master Marketing"],
                "schools_iut": ["IUT TC (Techniques de Commercialisation)", "IUT Information-Communication"],
                "fields": ["Marketing Digital", "Stratégie de Marque", "Communication des Entreprises"],
                "summaries": [
                    "Expert marketing orienté résultats, spécialisé dans l'acquisition client et l'optimisation des taux de conversion (CRO). Fort d'une expérience en pilotage de budgets publicitaires importants, je maîtrise l'ensemble du tunnel de vente digital, de la notoriété à la fidélisation. Passionné par l'analyse de données, je transforme les insights consommateurs en stratégies de croissance concrètes.",
                    "Stratège en communication et marketing avec une forte appétence pour le branding et le storytelling. J'accompagne les marques dans leur transformation digitale en créant des expériences omnicanales cohérentes. Mon approche repose sur une veille constante des tendances sociales et une gestion rigoureuse des KPIs pour garantir le ROI des campagnes.",
                    "Spécialiste Growth Marketing (Growth Hacker) focalisé sur l'expérimentation rapide (A/B testing) pour optimiser toutes les étapes du tunnel AARRR. Je combine créativité et analyse de données pour identifier de nouveaux canaux d'acquisition et réduire drastiquement les coûts par lead (CPA).",
                    "Responsable Marketing de Contenu (Content Manager) expert en stratégie éditoriale B2B et B2C. Je conçois des contenus à forte valeur ajoutée (livres blancs, articles de blog, webinaires) qui positionnent la marque comme leader d'opinion tout en générant un flux régulier de leads qualifiés (Inbound Marketing).",
                    "Expert SEO (Search Engine Optimization) technique et sémantique. J'optimise l'architecture des sites web, mets en place des stratégies de netlinking pointues et cible les cocons sémantiques pour propulser l'entreprise en première page des moteurs de recherche sur des mots-clés hautement concurrentiels.",
                    "Performance Marketer et Media Buyer avec une solide maîtrise des plateformes publicitaires (Google Ads, Meta Ads, LinkedIn Ads). Je gère d'importants budgets médias avec un focus obsessionnel sur le Retour sur Investissement Publicitaire (ROAS) et l'optimisation algorithmique des campagnes.",
                    "Manager CRM et Fidélisation (Customer Relationship Management). Je bâtis des parcours clients hyper-personnalisés et automatisés pour maximiser la LifeTime Value (LTV). Mon approche data-driven me permet de segmenter finement les bases de données et d'anticiper le taux d'attrition (churn).",
                    "Brand Strategist et Chef de Marque. Je définis l'identité visuelle, la voix et les valeurs de l'entreprise pour construire une image de marque forte et mémorable. Je coordonne des campagnes de communication 360° en veillant à la cohérence de l'image sur tous les points de contact."
                ],
                "actions": [
                    "Pilotage de campagnes Google Ads et Social Ads avec un budget mensuel de 50k€, générant une hausse de 30% des leads qualifiés.",
                    "Refonte de la stratégie de contenu SEO ayant permis de doubler le trafic organique du site web en l'espace de 6 mois.",
                    "Lancement d'un nouveau produit sur le marché européen, incluant l'étude de marché, le positionnement prix et le plan média.",
                    "Optimisation des scénarios d'automation marketing sur HubSpot, augmentant le taux d'ouverture des emails de 15%.",
                    "Coordination d'une équipe de 5 créatifs (graphistes, rédacteurs) pour la production des assets de campagne annuelle.",
                    "Analyse hebdomadaire des performances via Google Analytics et rédaction de rapports stratégiques pour la direction marketing.",
                    "Mise en place d'un programme de parrainage client ayant contribué à 10% du chiffre d'affaires total sur le dernier trimestre.",
                    "Négociation et gestion de partenariats avec des influenceurs majeurs du secteur, touchant une audience de plus de 500k abonnés.",
                    "Organisation d'événements de relations presse et lancements de produits physiques pour renforcer l'image de marque.",
                    "Audit complet de l'e-réputation de l'entreprise et mise en place d'une charte de modération pour les réseaux sociaux.",
                    "Développement d'outils de veille concurrentielle automatisés pour ajuster en temps réel le positionnement de l'offre.",
                    "Animation de workshops internes sur le Design Thinking pour favoriser l'innovation dans la conception des futurs services.",
                    "Conception et exécution de tests A/B multivariés sur les landing pages principales, augmentant le taux de conversion de lead de 22%.",
                    "Optimisation experte des stratégies d'enchères intelligentes sur Google Ads, améliorant le ROAS (Return On Ad Spend) de 150% en un trimestre.",
                    "Réalisation d'un audit SEO technique complet (Core Web Vitals, balisage, indexabilité) suivi de l'implémentation des recommandations correctives.",
                    "Création de workflows complexes de Lead Nurturing sur HubSpot, permettant de réchauffer les prospects froids et de multiplier par deux le taux de closing des ventes.",
                    "Pilotage d'une campagne d'influence sur TikTok et Instagram, générant plus de 3 millions de vues organiques et une rupture de stock en 48 heures.",
                    "Rédaction orientée conversion (Copywriting) pour les newsletters hebdomadaires, faisant passer le taux de clic moyen (CTR) de 2% à 8%.",
                    "Développement d'une stratégie de clusters sémantiques (Topic Clusters) ayant permis de positionner 40 nouveaux articles en Top 3 sur Google.",
                    "Lancement et animation d'une communauté en ligne d'utilisateurs bêta-testeurs via Discord pour récolter du feedback produit en direct.",
                    "Mise en place du suivi de conversion côté serveur (Server-Side Tracking) pour pallier la perte de données liée aux bloqueurs de publicités et aux cookies tiers.",
                    "Négociation d'espaces publicitaires (Display et Programmatique) et partenariats médias avec les principaux magazines en ligne du secteur.",
                    "Scraping de données ciblées sur LinkedIn et création de campagnes de Cold Emailing ultra-personnalisées avec un taux de réponse de 12%.",
                    "Organisation de A à Z de webinaires mensuels engageant en moyenne 500 participants en direct et alimentant la base de données de prospection."
                ]
            },
            
            "medecine": {
                "job_titles": ["Médecin Généraliste", "Interne en Médecine", "Chef de Clinique", "Médecin Urgentiste"],
                "skills": ["Diagnostic clinique", "Prescription médicale", "Gestion des urgences", "Sémiologie médicale", "Lecture d'ECG", "Télémédecine", "Éthique et Déontologie", "Dossier Médical Partagé"],
                "companies": ["AP-HP", "Hospices Civils de Lyon", "CHU de Bordeaux", "SOS Médecins", "Clinique Ramsay Santé", "Cabinet Médical Pluridisciplinaire"],
                "schools_inge": [
                    "Faculté de Médecine Paris Cité", 
                    "Sorbonne Université - Faculté de Médecine",
                    "Faculté de Médecine de Strasbourg",
                    "Faculté de Médecine de Montpellier-Nîmes",
                    "Aix-Marseille Université - Faculté des sciences médicales",
                    "Faculté de Médecine de Lyon Est",
                    "Faculté de Médecine de Lille"
                ],
                "schools_uni": [
                    "Université de Bordeaux - Collège des Sciences de la Santé",
                    "Université de Toulouse III - Paul Sabatier",
                    "Université de Lorraine - Faculté de Médecine de Nancy",
                    "Université de Rennes 1 - Faculté de Médecine",
                    "Université de Nantes - Faculté de Médecine",
                    "Université Côte d'Azur - Faculté de Médecine de Nice",
                    "Université de Grenoble Alpes - Faculté de Médecine",
                    "Université de Rouen Normandie",
                    "Université de Caen Normandie",
                    "Université de Tours - Faculté de Médecine"
                ],
                "schools_iut": ["IFSI (Soins Infirmiers)", "Institut de Formation en Santé"],
                "fields": ["Médecine Générale", "Urgences et Réanimation", "Santé Publique"],
                "summaries": [
                    "Praticien dévoué possédant une solide expérience en médecine aiguë et suivi de pathologies chroniques. Mon approche est centrée sur le patient, alliant rigueur scientifique et écoute active pour assurer une prise en charge globale et personnalisée. Habitué au travail en équipe pluridisciplinaire, je m'engage à maintenir l'excellence des soins dans le respect strict du secret médical.",
                    "Interne en fin de cursus avec une forte appétence pour la médecine d'urgence et la gestion de crise. Capable de prendre des décisions rapides dans des environnements à haute pression, je veille à la sécurité des patients et à la fluidité du parcours de soins. Mon parcours m'a permis de développer une expertise en diagnostic différentiel et en gestes techniques d'urgence.",
                    "Médecin pédiatre dévoué à la santé et au bien-être des enfants, de la naissance à l'adolescence. Je réalise les examens de suivi préventif, diagnostique et traite les pathologies aiguës ou chroniques pédiatriques, tout en rassurant et guidant les parents dans le développement de leur enfant.",
                    "Médecin du travail et de prévention, spécialiste de la santé au sein des environnements professionnels. J'évalue l'aptitude médicale des salariés, diagnostique les maladies professionnelles et accompagne les entreprises dans la prévention des risques psychosociaux (RPS) et ergonomiques (TMS).",
                    "Psychiatre orienté vers le diagnostic et le traitement des troubles de la santé mentale. Pratiquant une approche bio-psycho-sociale, j'élabore des projets thérapeutiques personnalisés (pharmacologie et psychothérapie) pour accompagner les patients souffrant de troubles anxieux, dépressifs ou psychotiques.",
                    "Chirurgien (interne/assistant) passionné par l'innovation au bloc opératoire et la chirurgie mini-invasive. Rigoureux et précis, je participe activement aux interventions chirurgicales programmées et d'urgence, tout en assurant une prise en charge optimale en période pré et post-opératoire.",
                    "Médecin chercheur (Investigateur Clinique) évoluant à la frontière entre la pratique clinique et la recherche académique. Je pilote des essais cliniques de phase 2 et 3, recrutant des patients pour tester de nouvelles stratégies thérapeutiques en oncologie dans le respect des bonnes pratiques cliniques (BPC).",
                    "Gériatre spécialisé dans la prise en charge globale des patients âgés polypathologiques. J'interviens en EHPAD ou en unité de soins de suite (SSR) pour prévenir la perte d'autonomie, évaluer les troubles cognitifs et ajuster les prescriptions afin de limiter la iatrogénie médicamenteuse."
                ],
                "actions": [
                    "Réalisation de plus de 25 consultations quotidiennes, incluant le diagnostic, le traitement et le suivi thérapeutique des patients.",
                    "Prise en charge autonome des urgences vitales au sein du SAU, avec réalisation de gestes de réanimation cardiorespiratoire.",
                    "Coordination des soins pour les patients atteints de maladies chroniques (diabète, HTA) en lien avec les spécialistes hospitaliers.",
                    "Mise en place de protocoles de télémédecine pour assurer la continuité des soins dans les zones de désert médical.",
                    "Participation active aux réunions de concertation pluridisciplinaire (RCP) pour les cas cliniques complexes.",
                    "Encadrement et formation pratique des étudiants hospitaliers (externes) lors de leurs stages cliniques en service.",
                    "Rédaction rigoureuse des observations médicales et des comptes rendus de sortie sur le logiciel métier (Orbis/DxCare).",
                    "Animation de séances de prévention (sevrage tabagique, vaccination) auprès de populations à risque.",
                    "Gestion des prescriptions médicamenteuses en veillant à l'absence d'interactions dangereuses et au respect des recommandations HAS.",
                    "Participation aux gardes de 24h et astreintes médicales, garantissant la permanence des soins de l'établissement.",
                    "Réalisation de petites chirurgies ambulatoires et soins de plaies complexes (sutures, pansements spécifiques).",
                    "Accompagnement des familles dans le cadre de l'annonce de diagnostics graves et mise en place de soins palliatifs.",
                    "Réalisation de consultations pédiatriques de dépistage précoce (audition, vision, développement psychomoteur) et administration des vaccins obligatoires.",
                    "Mise en place de visites de postes de travail en usine pour analyser l'ergonomie et proposer des aménagements pour les salariés en situation de handicap.",
                    "Conduite d'entretiens cliniques approfondis pour l'évaluation du risque suicidaire aux urgences psychiatriques, suivis d'orientations adaptées.",
                    "Assistance opératoire en tant que premier aide sur plus de 100 chirurgies viscérales par cœlioscopie (appendicectomies, cholécystectomies).",
                    "Collecte rigoureuse des événements indésirables (pharmacovigilance) et saisie des données cliniques des patients inclus dans un essai thérapeutique international.",
                    "Coordination de réunions de synthèse gériatrique avec les kinésithérapeutes, diététiciens et assistantes sociales pour préparer le retour à domicile du patient.",
                    "Pratique de gestes techniques en chambre (ponctions lombaires, ponctions d'ascite, gaz du sang) dans le strict respect des règles d'asepsie.",
                    "Mise en place d'un protocole de sédation proportionnée et accompagnement psychologique des familles dans l'unité de soins palliatifs.",
                    "Élaboration d'évaluations gérontologiques standardisées (EGS) pour dépister les fragilités, les risques de chute et les troubles de la mémoire (MMS).",
                    "Réalisation d'échographies cliniques d'urgence (POCUS/FAST) au lit du patient pour éliminer rapidement une pathologie vitale (épanchement, hémorragie).",
                    "Animation d'ateliers de psychoéducation pour aider les patients atteints de troubles bipolaires à mieux repérer les signes précurseurs de rechute.",
                    "Participation active aux gardes de nuit en réanimation polyvalente, avec prise en charge hémodynamique et respiratoire des patients instables."
                ]
            },

            "rh": {
                "job_titles": ["Talent Acquisition Specialist", "Responsable Ressources Humaines", "HR Business Partner (HRBP)", "Chargé de Recrutement IT", "Gestionnaire Paie et RH"],
                "skills": ["Sourcing", "Entretiens structurés", "Droit du travail", "Gestion de la paie", "SIRH (Workday, Lucca)", "Marque employeur", "Onboarding", "GPEC", "Relations sociales (CSE)", "Formation"],
                "companies": ["Capgemini", "Doctolib", "L'Oréal", "Criteo", "Thales", "Orange", "Cabinet de recrutement Michael Page"],
                "schools_inge": ["CIFFOP", "Sciences Po Paris", "HEC Paris - Majeure RH"], 
                "schools_uni": ["Université Paris 1 Panthéon-Sorbonne", "IAE Paris", "Université de Strasbourg - Master RH"],
                "schools_iut": ["IUT GEA (Gestion des Entreprises)", "Licence Pro Métiers de la GRH", "IUT Carrières Juridiques"],
                "fields": ["Ressources Humaines", "Droit Social", "Management des Organisations"],
                "summaries": [
                    "Professionnel des Ressources Humaines passionné par le développement des talents et l'accompagnement des managers. Doté d'une forte expertise en recrutement (notamment sur des profils pénuriques IT) et en droit social, je m'attache à construire une marque employeur forte. Mon objectif est d'aligner la stratégie RH avec les objectifs business de l'entreprise tout en garantissant un climat social serein.",
                    "HR Business Partner polyvalent avec plus de 5 ans d'expérience dans l'accompagnement de la croissance d'entreprises tech. J'interviens sur l'ensemble du cycle de vie des collaborateurs : de l'onboarding optimisé à la gestion des carrières (GPEC), en passant par la structuration des politiques de rémunération. Rigoureux et à l'écoute, je suis un véritable partenaire de confiance pour les équipes opérationnelles.",
                    "Campus Manager et spécialiste des relations écoles. Je construis des partenariats stratégiques avec les meilleures écoles d'ingénieurs et de commerce pour attirer les jeunes talents. Je pilote la politique des stages et alternances en créant des programmes d'intégration attractifs pour les étudiants.",
                    "Spécialiste Compensation & Benefits (Rémunération et Avantages Sociaux). J'analyse le marché et conçois des politiques salariales compétitives et équitables. Je gère les campagnes de révisions salariales et optimise les packages globaux pour fidéliser les collaborateurs clés de l'entreprise.",
                    "Responsable Formation (Learning & Development Manager). Passionné par la montée en compétences, je déploie le plan de formation annuel et administre les plateformes e-learning (LMS). Je conçois des parcours pédagogiques sur-mesure pour accompagner la transformation des métiers.",
                    "Responsable Diversité & Inclusion (D&I). Je conçois et mets en œuvre des stratégies visant à promouvoir l'égalité professionnelle, le handicap et l'inclusion intergénérationnelle. J'anime des actions de sensibilisation pour garantir un environnement de travail respectueux et équitable.",
                    "Chef de projet SIRH (Système d'Information Ressources Humaines). J'interface la fonction RH avec les outils digitaux en pilotant le déploiement ou l'optimisation des logiciels (Workday, SAP SuccessFactors). J'assure la fiabilité des données et forme les utilisateurs aux nouveaux processus.",
                    "Manager du développement des talents (Talent Management). J'accompagne les managers dans la détection des hauts potentiels (HiPo), l'élaboration des plans de succession et la conduite des entretiens d'évaluation annuels pour dynamiser les évolutions de carrières internes."
                ],
                "actions": [
                    "Pilotage du cycle de recrutement complet pour des profils Tech et Produit, aboutissant à plus de 40 embauches en CDI sur l'année.",
                    "Déploiement d'un nouveau logiciel SIRH (Lucca) pour automatiser la gestion des congés et le suivi des temps de travail.",
                    "Refonte totale du processus d'Onboarding, ce qui a permis de réduire le taux de turnover des nouveaux collaborateurs de 15% lors de la période d'essai.",
                    "Préparation et co-animation des réunions mensuelles avec le Comité Social et Économique (CSE), en garantissant un dialogue social constructif.",
                    "Conception et déploiement du plan de développement des compétences (plan de formation) avec un budget annuel alloué de 150 000 euros.",
                    "Gestion administrative du personnel (DPAE, contrats de travail, avenants) et supervision des éléments variables de paie pour 200 salariés.",
                    "Mise en place d'une stratégie de sourcing multicanal (LinkedIn Recruiter, Github, cooptation) pour chasser des profils pénuriques (Data, DevOps).",
                    "Organisation d'événements liés à la Marque Employeur (salons étudiants, meetups) ayant doublé le volume de candidatures spontanées entrantes.",
                    "Accompagnement quotidien des managers sur les problématiques de droit du travail (sanctions disciplinaires, ruptures conventionnelles, licenciements).",
                    "Création d'une grille de rémunération transparente et mise en place d'une politique d'avantages sociaux (mutuelle, tickets restaurant).",
                    "Conduite d'une cartographie des emplois et des compétences (GPEC) pour anticiper les besoins en recrutement sur les 3 prochaines années.",
                    "Mise en place d'enquêtes de satisfaction interne (eNPS) trimestrielles et création de plans d'action pour améliorer la Qualité de Vie au Travail (QVT).",
                    "Réalisation d'audits de rémunération (Benchmarking) face au marché concurrentiel, permettant de réajuster les salaires de 30 profils critiques pour éviter les démissions.",
                    "Négociation de partenariats exclusifs avec 5 universités cibles, incluant le parrainage de promotions et l'organisation d'études de cas métiers en amphithéâtre.",
                    "Déploiement global d'une nouvelle plateforme LMS (Learning Management System), offrant un catalogue de 500 formations digitalisées en libre accès aux salariés.",
                    "Pilotage d'actions en faveur du handicap (RQTH), augmentant le taux d'emploi direct de personnes en situation de handicap de 3% à 5,5% en deux ans.",
                    "Modélisation et nettoyage des bases de données RH (Data Analytics) pour créer des tableaux de bord automatisés mesurant le taux d'absentéisme et de turnover.",
                    "Conduite des entretiens de départ (Exit Interviews) pour tous les collaborateurs démissionnaires, avec analyse des motifs profonds restituée à la direction générale.",
                    "Organisation logistique et animation de sessions d'Assessment Centers pour évaluer les soft skills de candidats finaux sur des postes de direction.",
                    "Refonte de la classification des emplois (grilles de classification) suite à la mise en application de la nouvelle convention collective nationale de la métallurgie.",
                    "Conception d'un programme de 'Mentoring' interne croisé mettant en relation des directeurs expérimentés avec de jeunes talents identifiés comme hauts potentiels.",
                    "Préparation des dossiers obligatoires annuels (Index Égalité Femmes-Hommes, Bilan Social) et communication transparente des résultats aux partenaires sociaux.",
                    "Audit de la conformité du paramétrage de la paie en collaboration étroite avec l'éditeur du logiciel SIRH, permettant de corriger des anomalies de cotisations sociales.",
                    "Animation de webinaires internes dédiés au bien-être mental et à la prévention de l'épuisement professionnel (Burn-Out) en période de forte activité."
                ]
            }
        }
 
        self.first_names = [
            "Thomas", "Samy", "Emma", "Lucas", "Léa", "Hugo", "Chloé", "Léo", "Camille", "Nicolas", 
            "Antoine", "Juliette", "Gabriel", "Raphaël", "Arthur", "Louis", "Jules", "Adam", "Maël", 
            "Jade", "Louise", "Ambre", "Alice", "Alba", "Rose", "Anna", "Mia", "Lina", "Noah", 
            "Eden", "Gabin", "Isaac", "Léon", "Malo", "Naël", "Paul", "Aaron", "Liam", "Julia", 
            "Léna", "Inès", "Aya", "Léonie", "Mila", "Iris", "Alexandre", "Victor", "Sarah", "Eva", "Clara"
        ]
        self.last_names = [
            "Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", 
            "Simon", "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", 
            "Morel", "Girard", "André", "Lefèvre", "Mercier", "Dupont", "Lambert", "Guillaume", "Benoit", "Marin", 
            "Garnier", "Chevalier", "François", "Legrand", "Gauthier", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", 
            "Roussel", "Nicolas", "Perrin", "Mathieu", "Clement", "Gautier", "Boyer", "Fontaine", "Robin", "Masson"
        ]
 
    def _random_date(self, year: int, after_month: int = 1) -> tuple:
        """Retourne un (mois, année) aléatoire dans l'année donnée,
        avec le mois >= after_month pour éviter tout chevauchement."""
        month = random.randint(after_month, 12)
        return month, year
 
    def generate_experience(self, job_title: str, archetype_data: dict, graduation_year: int) -> List[Dict]:
        nb_actions_needed = 3 + 4 + 4 
        if len(archetype_data["actions"]) < nb_actions_needed:
            raise ValueError(
                f"L'archétype doit avoir au moins {nb_actions_needed} actions, "
                f"il en a {len(archetype_data['actions'])}."
            )
 
        actions_disponibles = random.sample(archetype_data["actions"], len(archetype_data["actions"]))
 
        # --- Exp 3 : stage/alternance avant l'obtention du diplôme ---
        start_year_exp3 = graduation_year - random.randint(1, 2)
        start_month_exp3 = random.randint(1, 12)
        end_month_exp3 = random.randint(start_month_exp3 if start_year_exp3 == graduation_year else 1, 12)
 
        prefix = random.choice(["Alternance", "Stage"])
        exp3 = {
            "position": f"{prefix} — Assistant {job_title}",
            "company": random.choice(archetype_data["companies"]),
            "start_date": f"{start_month_exp3:02d}/{start_year_exp3}",
            "end_date": f"{end_month_exp3:02d}/{graduation_year}",
            "description": " ".join([actions_disponibles.pop() for _ in range(3)])
        }
 
        # --- Exp 2 : premier poste, commence après la fin du stage ---
        end_year_exp2 = graduation_year + random.randint(1, 2)
        current_year = datetime.date.today().year
        if end_year_exp2 >= current_year:
            end_year_exp2 = current_year - 1
 
        start_month_exp2 = random.randint(end_month_exp3, 12)
        end_month_exp2 = random.randint(1, 12)
 
        exp2 = {
            "position": job_title,
            "company": random.choice(archetype_data["companies"]),
            "start_date": f"{start_month_exp2:02d}/{graduation_year}",
            "end_date": f"{end_month_exp2:02d}/{end_year_exp2}",
            "description": " ".join([actions_disponibles.pop() for _ in range(4)])
        }
 
        # --- Exp 1 : poste confirmé, commence après la fin du poste précédent ---
        start_month_exp1 = random.randint(end_month_exp2, 12)
 
        exp1 = {
            "position": f"{job_title} / Confirmé",
            "company": random.choice(archetype_data["companies"]),
            "start_date": f"{start_month_exp1:02d}/{end_year_exp2}",
            "end_date": "Aujourd'hui",
            "description": " ".join([actions_disponibles.pop() for _ in range(4)])
        }
 
        return [exp1, exp2, exp3]
 
    def generate_education(self, archetype_data: dict, graduation_year: int) -> List[Dict]:
        education = []
        chosen_field = random.choice(archetype_data["fields"])

        if "Médecine" in chosen_field or "Santé" in chosen_field or "Urgences" in chosen_field:
            school_uni = random.choice(archetype_data["schools_uni"])
            education.append({"degree": "Diplôme d'État de Docteur en Médecine", "field": chosen_field, "school": school_uni, "year": f"{graduation_year}"})
            education.append({"degree": "DFASM (Diplôme de Formation Approfondie)", "field": "Sciences Médicales", "school": school_uni, "year": f"{graduation_year - 3} - {graduation_year - 1}"})
            return education

        parcours_types = ["prepa_inge", "licence_master", "dut_inge", "bts_licence_pro", "but_master"]
        
        # Pour les RH et Marketing, on évite les diplômes d'ingénieur purs
        if "Ressources Humaines" in chosen_field or "Marketing" in chosen_field:
            parcours_types = ["licence_master", "bts_licence_pro", "but_master"]

        choix_parcours = random.choice(parcours_types)
 
        if choix_parcours == "prepa_inge":
            school_inge = random.choice(archetype_data["schools_inge"])
            education.append({"degree": "Diplôme d'Ingénieur", "field": chosen_field, "school": school_inge, "year": f"{graduation_year - 3} - {graduation_year}"})
            education.append({"degree": "Classes Préparatoires (CPGE)", "field": "Filière Scientifique", "school": "Lycée Scientifique", "year": f"{graduation_year - 5} - {graduation_year - 3}"})
 
        elif choix_parcours == "licence_master":
            school_uni = random.choice(archetype_data["schools_uni"])
            education.append({"degree": "Master", "field": chosen_field, "school": school_uni, "year": f"{graduation_year - 2} - {graduation_year}"})
            education.append({"degree": "Licence", "field": chosen_field, "school": school_uni, "year": f"{graduation_year - 5} - {graduation_year - 2}"})
 
        elif choix_parcours == "dut_inge":
            school_inge = random.choice(archetype_data["schools_inge"])
            school_iut = random.choice(archetype_data["schools_iut"])
            education.append({"degree": "Diplôme d'Ingénieur", "field": chosen_field, "school": school_inge, "year": f"{graduation_year - 3} - {graduation_year}"})
            education.append({"degree": "DUT", "field": chosen_field, "school": school_iut, "year": f"{graduation_year - 5} - {graduation_year - 3}"})
 
        elif choix_parcours == "bts_licence_pro":
            school_uni = random.choice(archetype_data["schools_uni"])
            school_iut = random.choice(archetype_data["schools_iut"])
            education.append({"degree": "Licence Professionnelle", "field": chosen_field, "school": school_uni, "year": f"{graduation_year - 1} - {graduation_year}"})
            education.append({"degree": "BTS", "field": chosen_field, "school": school_iut, "year": f"{graduation_year - 3} - {graduation_year - 1}"})
 
        elif choix_parcours == "but_master":
            school_uni = random.choice(archetype_data["schools_uni"])
            school_iut = random.choice(archetype_data["schools_iut"])
            education.append({"degree": "Master", "field": chosen_field, "school": school_uni, "year": f"{graduation_year - 2} - {graduation_year}"})
            education.append({"degree": "BUT", "field": chosen_field, "school": school_iut, "year": f"{graduation_year - 5} - {graduation_year - 2}"})
 
        return education
 
    def generate_profile(self, chosen_archetype: str) -> Dict:
        if chosen_archetype == "dev":
            chosen_archetype = random.choice(["dev_web", "data_ia", "game_dev", "bio_info", "devops", "cybersecu"])
        elif chosen_archetype == "random":
            chosen_archetype = random.choice(list(self.archetypes.keys()))
 
        data = self.archetypes[chosen_archetype]
        job_title = random.choice(data["job_titles"])
 
        graduation_year = random.randint(2018, 2024)
 
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
 
        cv = {
            "personal_info": {
                "first_name": first_name,
                "last_name": last_name,
                "email": f"{first_name.lower()}.{last_name.lower()}@email.com",
                "phone": f"06 {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}"
            },
            "job_title": job_title,
            "resume": random.choice(data["summaries"]),
            "skills": random.sample(data["skills"], min(8, len(data["skills"]))),
            "experience": self.generate_experience(job_title, data, graduation_year),
            "education": self.generate_education(data, graduation_year)
        }
        return cv
 
    def generate_pdf_latex(self, cv_data: dict, output_dir: str = None):
 
        script_dir = os.path.dirname(os.path.abspath(__file__))
 
        if output_dir is None:
            output_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "Templates_CV"))
 
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
 
        template_path = os.path.join(script_dir, "cv_template.tex")
 
        try:
            with open(template_path, "r", encoding="utf-8") as f:
                template_content = f.read()
        except FileNotFoundError:
            print(f"ERREUR : Le template 'cv_template.tex' est introuvable dans {script_dir}")
            return
 
        def safe_latex(text: str) -> str:
            """Échappe les caractères spéciaux LaTeX dans une chaîne brute."""
            return str(text).replace("&", "\\&").replace("#", "\\#").replace("%", "\\%")
 
        # safe_latex appliqué sur chaque champ individuel AVANT d'être injecté dans du LaTeX
        competences_latex = " $\\bullet$ ".join(
            [f"\\textbf{{{safe_latex(c)}}}" for c in cv_data['skills']]
        )
 
        experiences_latex = ""
        for exp in cv_data['experience']:
            position  = safe_latex(exp['position'])
            company   = safe_latex(exp['company'])
            start     = safe_latex(exp['start_date'])
            end       = safe_latex(exp['end_date'])
            desc      = safe_latex(exp['description'])
            experiences_latex += (
                f"\\noindent \\textbf{{{position}}} --- \\textit{{{company}}} "
                f"\\hfill \\textbf{{{start} à {end}}} \\\\\n"
                f"{desc} \\\\[0.3cm]\n"
            )
 
        formations_latex = ""
        for edu in cv_data['education']:
            degree = safe_latex(edu['degree'])
            field  = safe_latex(edu['field'])
            school = safe_latex(edu['school'])
            year   = safe_latex(edu['year'])
            formations_latex += (
                f"\\noindent \\textbf{{{degree} en {field}}} \\hfill \\textbf{{{year}}} \\\\\n"
                f"\\textit{{{school}}} \\\\[0.3cm]\n"
            )
 
        final_tex = template_content.replace("[[PRENOM]]",          safe_latex(cv_data['personal_info']['first_name']))
        final_tex = final_tex.replace("[[NOM]]",                    safe_latex(cv_data['personal_info']['last_name']))
        final_tex = final_tex.replace("[[JOB_TITLE]]",              safe_latex(cv_data['job_title']))
        final_tex = final_tex.replace("[[EMAIL]]",                  safe_latex(cv_data['personal_info']['email']))
        final_tex = final_tex.replace("[[PHONE]]",                  safe_latex(cv_data['personal_info']['phone']))
        final_tex = final_tex.replace("[[RESUME]]",                 safe_latex(cv_data['resume']))
        final_tex = final_tex.replace("[[BLOC_COMPETENCES]]",       competences_latex)
        final_tex = final_tex.replace("[[BLOC_EXPERIENCES]]",       experiences_latex)
        final_tex = final_tex.replace("[[BLOC_FORMATIONS]]",        formations_latex)
 
        titre_propre = cv_data['job_title'].replace(' ', '').replace('/', '-')
        base_filename = f"CV_{titre_propre}_{cv_data['personal_info']['last_name']}"
        tex_filepath = os.path.join(output_dir, f"{base_filename}.tex")
 
        with open(tex_filepath, "w", encoding="utf-8") as f:
            f.write(final_tex)
 
        try:
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-output-directory', output_dir, tex_filepath],
                capture_output=True, text=True
            )
            if result.returncode != 0:
                print(f"Erreur LaTeX pour {base_filename} :")
                print(result.stdout[-1000:])
            else:
                print(f"PDF créé : {titre_propre} : {base_filename}.pdf")
            
            
            for ext in [".aux", ".log", ".tex"]:
                temp_file = os.path.join(output_dir, f"{base_filename}{ext}")
                if os.path.exists(temp_file):
                    os.remove(temp_file)
        except Exception as e:
            print("Erreur d'exécution python :", e)
 
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur de CV Multi-Informatique")
    parser.add_argument('--nb',   type=int, default=1,
                        help="Nombre de CV")
    parser.add_argument('--type', type=str,
                        choices=['dev', 'dev_web', 'data_ia', 'game_dev', 'bio_info', 'devops', 'cybersecu', 'btp', 'marketing', 'medecine', 'rh', 'random'],
                        default='random', help="Archétype du CV")
 
    args = parser.parse_args()
    print(f"Lancement : Génération de {args.nb} CV(s) de type '{args.type}'...")
 
    generator = CVGenerator()
    for i in range(args.nb):
        cv_data = generator.generate_profile(chosen_archetype=args.type)
        generator.generate_pdf_latex(cv_data)
 
    print("Terminé !")