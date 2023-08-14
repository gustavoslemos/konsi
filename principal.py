import csv
import requests
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

url = 'https://dash.adjust.com/control-center/reports-service/csv_report'
headers = {
    'Authorization': 'Bearer ccKyFVLyg9DjvE53NmL-'
}
params = {
    'cost_mode': 'network',
    'app_token__in': 'sc3cizv3g83k',
    'date_period': '2023-08-10:2023-08-13',
    'dimensions': 'day,campaign_network,adgroup_network,creative_network',
    'metrics': 'cost,network_impressions,network_clicks,installs,iniciou cadastro_events,registro completo sms_events,usuário tem benefício inss_events,usuário é servidor govba_events,usuário é servidor govsp_events,usuário é servidor prefsp_events,usuário é servidor govmt_events,usuário é lead_events,aceitar oferta_events,proposta paga_events,primeira compra_events,primeira compra govba_events,primeira compra govsp_events,primeira compra govmt_events,primeira compra prefsp_events,primeira compra inss_events,recompra_events,all_revenue'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    
    csv_data = response.text

   
    temp_filename = 'dados_principal.csv'
    with open(temp_filename, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)

        
        csv_lines = csv_data.splitlines()

        for line in csv_lines:
            row = line.split(',')

            
            campaign_network = row[1]
            if "_" in campaign_network:
                creative_network = row[3]
                if "_" not in creative_network:
                    row[3] = "0_0_0_0_0_0_0_0_0_0"

                cost = row[4]
                if cost:
                    row[4] = cost.replace(".", ",")

                all_revenue = row[25]
                if all_revenue:
                    row[25] = all_revenue.replace(".", ",")

                csv_writer.writerow(row)

    import os
    os.rename(temp_filename, "dados_filtrados.csv")

    print("CSV filtrado com sucesso e salvo no arquivo 'dados_filtrados.csv'.")
else:
    print(f"Erro na solicitação: {response.status_code}")

# ESSA PARTE DO CÓDIGO EU VOU COMENTAR, POIS É NECESSÁRIO VALIDAR COM VCS SE VÃO QUERER CRIAR UMA PLANILHA DO ZERO EXPORTANDO OS DADOS DO INICIO ATÉ HOJE OU FAZER UMA ADIÇÃO AO QUE TEM

# csv_lines = csv_data.splitlines()
# csv_data_list = [line.split(',') for line in csv_lines]


# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
# client = gspread.authorize(credentials)


# spreadsheet = client.open("Ad data Konsi Lifetime")


# worksheet = spreadsheet.worksheet("raw 02 (corrigindo)")


# worksheet.append_rows(values=csv_data_list)

# print("CSV filtrado adicionado à planilha com sucesso.")