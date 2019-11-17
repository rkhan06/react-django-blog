import React from "react";
import Blog from "./Blog";
import BlogList from "./BlogList";
import { Route, Switch } from "react-router-dom";

class ContentBlock extends React.Component {
  render() {
    return (
      <div>
        <Switch>
          <Route path="/" exact component={BlogList} />
          <Route path="/blog/:id" component={Blog} />
        </Switch>
      </div>
    );
  }
}

export default ContentBlock;
