import socket
import time
from tabulate import tabulate

class PortScanner:
    def __init__(self, hostname, port_range):
        self.hostname = hostname
        self.port_range = port_range

    def scan_port(self, port):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.5)
        
        start_time = time.time()
        scan_result = cliente.connect_ex((self.hostname, port))
        end_time = time.time()
        response_time = end_time - start_time
        
        if scan_result == 0:
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "Desconhecido"
                
            return (port, service_name, response_time)
        else:
            return None
        
    
    def run_scan(self):
        results = []
        for port in self.port_range:
            result = self.scan_port(port)
            if result:
                results.append(result)
        
        return results 
    
    def save_results(self, results, filename):
        table_headers = ["Porta", "Serviço", "Tempo de Resposta"]
        table_data = [(result[0], result[1], result[2]) for result in results]
        
        with open(filename, 'w') as f:
            f.write(tabulate(table_data, headers=table_headers, tablefmt="grid"))



