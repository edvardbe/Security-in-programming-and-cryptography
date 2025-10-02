#include "httplib.h"
#include <iostream>
using namespace std;


int main() {
    httplib::Server svr;

    bool isAuthenticated = false;

    string html = R"(
            <!DOCTYPE html>
            <html>
            <head>
                <title>Login Page</title>
            </head>
            <body>
                <h2>Login</h2>
                <form action="/login" method="post">
                    Username: <input type="text" name="username"><br><br>
                    Password: <input type="password" name="password"><br><br>
                    <input type="submit" value="Login">
                </form>
            </body>
            </html>
        )";
    // Serve the login page (HTML form)
    svr.Get("/", [html, &isAuthenticated](const httplib::Request&, httplib::Response &res) {
        if(!isAuthenticated){
            res.set_redirect("/login");
        } else {
            res.set_content("<h1>Login successful!</h1>", "text/html");
        }
        
    });

    svr.Get("/login", [html, &isAuthenticated](const httplib::Request&, httplib::Response &res) {
        if(!isAuthenticated){
            res.set_content(html, "text/html");
        } else { 
            res.set_redirect("/");
        }
    });

    // Handle form submission
    svr.Post("/login", [html, &isAuthenticated](const httplib::Request &req, httplib::Response &res) {
        auto username = req.get_param_value("username");
        auto password = req.get_param_value("password");
        
        if (username == "admin" && password == "1234") {
            isAuthenticated = true;
            res.set_redirect("/");
        } else {
            res.set_content(html + "<h1>Invalid credentials</h1>", "text/html");
        }
    });

    cout << "Server is running at http://localhost:8080\n";
    svr.listen("0.0.0.0", 8080);
    return 0;
}
