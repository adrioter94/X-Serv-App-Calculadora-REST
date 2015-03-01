#!/usr/bin/python

import webappmulti


class operacion(webappmulti.app):

    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.resultado = 0

    def parse(self, request, rest):
        verb = request.split()[0][0:]
        body = request.split('\r\n\r\n')[-1]

        return (verb, body)

    def process(self, parsedRequest):
        verb = parsedRequest[0]
        body = parsedRequest[1]
        if verb == "GET":
            return ("200 OK", "<html><body>" + str(self.resultado) +
                    " </body></html>")
        elif verb == "PUT":
            try:
                params = parsedRequest[1].split(self.signo())
                self.op1 = int(params[0])
                self.op2 = int(params[1])
                self.resultado = self.operate(self.op1, self.op2)
                return ("200 OK", "<html><body>" + str(self.resultado) +
                        " </body></html>")

            except ValueError:
                self.resultado = 0
                return ("400 Error", "<html><body>" +
                        "El recurso no concuerda con la operacion" +
                        "</body></html>")

        else:
            return ("400 Error", "<html><body>" + verb +
                    " no permititdo " + " </body></html>")

    def operate(self, op1, op2):
        return None

    def signo(self):
        return None


class suma(operacion):

    def operate(self, op1, op2):
        return self.op1 + self.op2

    def signo(self):
        return "+"


class resta(operacion):

    def operate(self, op1, op2):
        return self.op1 - self.op2

    def signo(self):
        return "-"


class multi(operacion):

    def operate(self, op1, op2):
        return self.op1 * self.op2

    def signo(self):
        return "*"


class div(operacion):

    def operate(self, op1, op2):
        return self.op1 / self.op2

    def signo(self):
        return "/"

if __name__ == "__main__":
    suma = suma()
    resta = resta()
    multi = multi()
    div = div()
    testWebApp = webappmulti.webApp("localhost", 1234, {'/suma': suma,
                                                        '/resta': resta,
                                                        '/multi': multi,
                                                        '/div': div})
