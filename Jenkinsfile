pipeline {
    agent any

    environment {
       
        GIT_URL    = 'https://github.com/abdellatifabb/loganalyzer.git'
        GIT_BRANCH = 'main'
    }

    stages {
        // -----------------------------
        // 1) START : message de début
        // -----------------------------
        stage('Start') {
            steps {
                echo "Début de l’analyse des logs (Log Analyzer CLI)"
            }
        }

        // --------------------------------
        // 2) CHECKOUT : cloner le projet
        // --------------------------------
        stage('Checkout') {
            steps {
                // On clone le dépôt complet dans le workspace Jenkins
                git branch: "${GIT_BRANCH}", url: "${GIT_URL}"
            }
        }

        stage('Setup Python') {
            steps {
                script {
                    // Vérifier la version de Python installée sur l’agent
                    sh 'python3 --version'

                    // Mettre à jour pip et installer les dépendances du projet si requirements.txt existe
                    sh '''
                        python3 -m pip install --upgrade pip
                        if [ -f "requirements.txt" ]; then
                            pip install -r requirements.txt
                        fi
                    '''
                }
            }
        }

        // ------------------------------------------------
        // 4) ANALYZE : lancer votre script log_analyzer.py
        // ------------------------------------------------
        stage('Analyze') {
            steps {
                script {
                    // Si vous disposez déjà d’un fichier de logs dans votre repo (e.g. logs/sample.log),
                    // vous pouvez l’utiliser directement. Sinon, on crée un exemple basique en pipeline :
                    sh '''
                        # Exemple : création d’un petit fichier de logs pour tester le script
                        cat <<EOF > sample.log
                        2025-05-30 12:00:01 ERROR Exemple d'erreur
                        2025-05-30 12:00:02 INFO Exemple d'information
                        2025-05-30 12:00:03 WARNING Exemple d'avertissement
                        2025-05-30 12:00:04 info Minuscule info (vérifie la casse)
                        EOF

                        # Exécution du script en passant en entrée sample.log et en écrivant le résumé dans result.txt
                        python3 logAnalyzer.py -i sample.log -o result.txt

                        # On affiche le contenu de result.txt dans la console Jenkins pour vérification
                        echo "=== Contenu de result.txt ==="
                        cat result.txt
                        echo "============================="
                    '''
                }
            }
        }
        stage('End') {
            steps {
                echo "Fin du pipeline Log Analyzer"
            }
        }
    }

    post {
        always {
            echo "Le pipeline est terminé (statut = ${currentBuild.currentResult})."
        }
        failure {
            echo "❌ Le pipeline a échoué. Consultez les logs ci-dessus pour plus d’informations."
        }
        success {
            echo "✅ Le pipeline s’est exécuté avec succès !"
        }
    }
}
