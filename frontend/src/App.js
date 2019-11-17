import React from "react";
import NavBar from "./components/NavBar";
import ContentBlock from "./components/ContentBlock";
import { BrowserRouter as Router } from "react-router-dom";

class App extends React.Component {
  render() {
    return (
      <div>
        <Router>
          <NavBar />
          <ContentBlock />
        </Router>
      </div>
    );
  }
}

export default App;
