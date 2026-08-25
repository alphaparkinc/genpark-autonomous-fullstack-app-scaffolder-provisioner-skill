from client import AutonomousFullstackAppScaffolderProvisionerClient

def main():
    client = AutonomousFullstackAppScaffolderProvisionerClient()
    res = client.scaffold_and_deploy_autonomous_app('Create an AI podcast clipping tool with automatic Whisper captions and ffmpeg rendering')
    print('Deployment: ' + res['deployment_job_id'] + ' | ' + res['app_title'])
    print('Schema: ' + res['database_schema_migrated'] + ' (Endpoints: ' + str(res['backend_endpoints_provisioned']) + ', Routes: ' + str(res['frontend_routes_compiled']) + ')')
    print('Live App: ' + res['live_production_https_url'] + ' | Autonomous Pass: ' + str(res['zero_human_intervention_build_verified']))

if __name__ == '__main__':
    main()
