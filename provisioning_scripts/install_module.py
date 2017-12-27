import erppeek
# You can use this client if you have Erppeek installed and have a erppeek.ini file
# client = erppeek.Client.from_config('ErpPeekDemoDatabase')
# The alternative is by specifying the settings by command
server = 'http://localhost:8069'
database = 'shadow'
admin_user = 'admin'
admin_password = 'odoo'


client = erppeek.Client(server, database, admin_user, admin_password)

modules = ['l10n_ec', 'account_invoicing', 'l10n_ec_partner', 'crm']

for module in modules:
    modules_installed = client.modules(module, installed=False)
    if module in modules_installed['uninstalled']:
        client.install(module)
        print("The module " + module + " was installed ")
