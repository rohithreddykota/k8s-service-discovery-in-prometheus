import http.server

from prometheus import Counter, exposition

COUNTER_NAME = "request_count"
REQUEST_COUNT = Counter(COUTNER_NAME, 'Count', ['endpoint'])

class RequestsHandler(exposition.MetricsHandler):
    
    def do_GET(self):
        if self.path not in ('/foo', '/bar', '/metrics'):
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('404: Not Found'.encode())
            return
        
        if self.path in ('/foo', '/bar'):
            REQUEST_COUNT.labels(endpoint=self.path).inc()
            current_count = self._get_current_count()
            self.response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Current Count: [{self.path}] {current_count}'.encode())
            return
        else:
            return super().do_GET()




