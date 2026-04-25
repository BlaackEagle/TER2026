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
                    "Ingénieur logiciel polyvalent possédant une maîtrise approfondie du cycle de développement complet, de l'analyse fonctionnelle des besoins à la mise en production continue (CI/CD). Je suis particulièrement à l'aise dans les environnements agiles et j'excelle dans la résolution de problèmes algorithmiques complexes. J'ai activement participé à la migration d'architectures monolithiques vers des écosystèmes microservices basés sur le cloud, maximisant ainsi les performances globales et la fiabilité de systèmes critiques."
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
                    "Mise en place d'un système de cache distribué avec Redis, diminuant la latence des requêtes API récurrentes de plus de 60%."
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
                    "Expert en Sécurité des Systèmes d'Information avec une forte appétence pour l'analyse des vulnérabilités et la gestion de crises cyber. Opérant régulièrement au sein de centres de supervision de sécurité (SOC), j'ai développé une grande réactivité pour endiguer les compromissions. Rigoureux et curieux, je réalise une veille technologique constante pour anticiper les nouvelles méthodes des attaquants (APT)."
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
                    "Audit de configuration des équipements de sécurité (firewalls, proxys, WAF) pour s'assurer du strict respect des recommandations de l'ANSSI."
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
                    "Ingénieur IA passionné par le Traitement du Langage Naturel (NLP) et la Computer Vision. J'aide à transformer des données brutes en insights actionnables grâce à des architectures de réseaux de neurones complexes, tout en assurant leur mise en production via des API performantes. Convaincu par l'approche MLOps, je veille au maintien des performances des modèles tout au long de leur cycle de vie."
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
                    "Mise en place d'une architecture de Feature Store centralisée, facilitant la réutilisation des variables entre les différentes équipes Data."
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
                    "Développeur Gameplay polyvalent avec 5 ans d'expérience dans la création d'expériences ludiques immersives. J'aime collaborer étroitement avec les Game Designers et les artistes techniques pour donner vie à des mécaniques de jeu fluides, intuitives et robustes, en m'assurant que l'expérience manette en main soit toujours parfaitement peaufinée."
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
                    "Portage complet du moteur de jeu vers les consoles nouvelle génération (PS5, Xbox Series X), en exploitant au maximum les architectures SSD."
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
                    "Ingénieur spécialisé dans le traitement des données de santé. Je conçois des pipelines d'analyse automatisés et robustes pour séquencer l'ADN et identifier des biomarqueurs. Passionné par la recherche biomédicale, j'évolue à l'interface entre la médecine de précision et la data science, tout en respectant strictement les normes de confidentialité des données patients (RGPD, HDS)."
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
                    "Automatisation des rapports de diagnostic génétique à l'aide de scripts RMarkdown, garantissant une traçabilité totale pour les audits de santé."
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
                    "Site Reliability Engineer passionné par la haute disponibilité et la performance des systèmes distribués. J'interviens sur la sécurisation, le monitoring et la scalabilité des serveurs cloud pour garantir un taux de disponibilité (SLA) de 99,99% sur les applications critiques. Mon but est de construire des infrastructures capables de résister à n'importe quel incident."
                ],
                "actions": [
                    "Conception d'une infrastructure cloud résiliente sur AWS via Terraform (IaC), assurant une haute disponibilité des services et une scalabilité horizontale automatique.",
                    "Mise en place de pipelines d'intégration et de déploiement continus (CI/CD) sur GitLab automatisant l'ensemble des tests et le déploiement sur les clusters Kubernetes.",
                    "Implémentation d'un système de monitoring complet avec Prometheus et Grafana, réduisant le temps de détection des pannes (MTTD) de 60%.",
                    "Migration de 50 applications legacy vers une architecture conteneurisée sous Docker, réduisant drastiquement les coûts d'hébergement annuels.",
                    "Automatisation du provisionnement et de la configuration des serveurs Linux à l'aide de playbooks Ansible, éliminant les erreurs manuelles.",
                    "Mise en place d'une stratégie de sauvegarde automatisée (Disaster Recovery Plan) avec des tests de restauration trimestriels réussis à 100%.",
                    "Audit de l'infrastructure cloud et application des principes du FinOps, permettant une réduction de la facture mensuelle AWS de 25%.",
                    "Gestion et sécurisation des secrets de l'entreprise via HashiCorp Vault, avec rotation automatique des clés d'accès des API tierces.",
                    "Astreinte technique (On-call) et résolution d'incidents critiques en production de niveau 3 (N3), avec rédaction de post-mortems détaillés (blameless).",
                    "Déploiement d'une politique de sécurité 'Zero Trust', incluant la gestion stricte des identités (IAM) et le chiffrement des données au repos.",
                    "Mise en place d'une architecture de journalisation centralisée (ELK Stack), facilitant l'analyse des logs et le diagnostic des anomalies en production.",
                    "Organisation de sessions de formation internes (Tech Talks) sur les bonnes pratiques de conteneurisation et l'usage optimal de Git."
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
                    "Expert en gestion de chantiers et en direction de travaux, je mets mon savoir-faire au service de projets de construction ambitieux. Ayant évolué au sein de grands groupes du BTP, j'ai acquis une méthodologie rigoureuse dans l'optimisation des modes opératoires et l'allocation des ressources. Habitué à gérer des situations complexes, je garantis une communication transparente avec la maîtrise d'ouvrage."
                ],
                "actions": [
                    "Supervision des équipes d'exécution sur le chantier et gestion des plannings d'intervention, assurant une parfaite synchronisation entre le gros œuvre et le second œuvre.",
                    "Coordination stratégique avec 15 entreprises sous-traitantes et les bureaux d'études techniques pour garantir la conformité architecturale et structurelle du projet.",
                    "Suivi financier rigoureux d'un budget global de plus de 5 millions d'euros, incluant l'optimisation des achats de matériaux et la négociation des avenants.",
                    "Application stricte de la politique Qualité, Sécurité, Environnement (QSE) sur site, conduisant à l'obtention de zéro accident de travail avec arrêt.",
                    "Rédaction hebdomadaire des rapports d'avancement de chantier, animation des réunions de pilotage et présentation des indicateurs de performance (KPI).",
                    "Pilotage complet des opérations de levée des réserves lors de la livraison du bâtiment, garantissant l'entière satisfaction du client final.",
                    "Réponse technique aux appels d'offres (chiffrage, métré, proposition de variantes techniques) ayant permis de remporter 3 marchés publics majeurs.",
                    "Implantation topographique sur site et vérification quotidienne du bon respect des plans d'exécution fournis par le bureau d'études béton armé.",
                    "Gestion des démarches administratives complexes (autorisations de voirie, DT/DICT) et maintien de bonnes relations avec les riverains du chantier.",
                    "Conduite des réunions de chantier inter-entreprises hebdomadaires, avec rédaction et diffusion des comptes rendus d'avancement à l'ensemble des parties.",
                    "Supervision des études d'exécution et validation des plans de synthèse, permettant d'anticiper les conflits entre les réseaux CVC, plomberie et électricité.",
                    "Gestion des relations avec les bureaux de contrôle (Apave, Socotec) pour garantir l'obtention des attestations de conformité finale avant la livraison."
                ]
            }
        }
 
        self.first_names = ["Thomas", "Samy", "Emma", "Lucas", "Léa", "Hugo", "Chloé", "Léo", "Camille", "Nicolas", "Antoine", "Juliette"]
        self.last_names = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon", "Laurent"]
 
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
        parcours_types = ["prepa_inge", "licence_master", "dut_inge", "bts_licence_pro", "but_master"]
        choix_parcours = random.choice(parcours_types)
 
        chosen_field = random.choice(archetype_data["fields"])
 
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
                        choices=['dev', 'dev_web', 'data_ia', 'game_dev', 'bio_info', 'devops', 'cybersecu', 'btp', 'random'],
                        default='random', help="Archétype du CV")
 
    args = parser.parse_args()
    print(f"Lancement : Génération de {args.nb} CV(s) de type '{args.type}'...")
 
    generator = CVGenerator()
    for i in range(args.nb):
        cv_data = generator.generate_profile(chosen_archetype=args.type)
        generator.generate_pdf_latex(cv_data)
 
    print("Terminé !")