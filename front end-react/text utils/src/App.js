import "./App.css";
import Navbar from "./components/Navbar";
import TextForm from "./components/Textform";
import React, { useState } from "react";
import Alert from "./components/Alert";
import About from "./components/About";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
  const [mode, setMode] = useState("light"); // Whether dark mode is enabled or not
  const [alert, setalert] = useState(null);
  const showalert=(message,type)=>{
    setalert({
      msg: message,
      type:type,
    })
    setTimeout(() => {
      setalert("null")
    },1500);
  }

  const toggleMode = () => {
    if (mode === "light") {
      setMode("dark");
      document.body.style.backgroundColor = "#042743";
      showalert("darkmode has been enabled","success")
    } else {
      setMode("light");
      document.body.style.backgroundColor = "white";
      showalert("lightmode has been enabled","success");
    }
  };
  return (
    <>
      <Router>
        <Navbar title="TextUtils" mode={mode} toggleMode={toggleMode} />
        <Alert alert={alert} />
        <div className="container my-3">
          <Switch>
            <Route exact path="/about">
              <About mode={mode} />
            </Route>

            <Route exact path="/">
              <TextForm
                heading="Enter the text to analyze below"
                mode={mode}
                showalert={showalert}
              />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default App;
