import React from "react";
import axios from "axios";

class Blog extends React.Component {
  constructor() {
    super();
    this.state = {
      blog: {}
    };
  }
  componentDidMount() {
    axios
      .get(`/api/blogs/${this.props.match.params.id}`)
      .then(res => {
        this.setState({ blog: res.data });
        console.log(res.data);
      })
      .catch(console.log);
  }
  render() {
    return (
      <div className="col-sm-10 ">
        <h1>{this.state.blog.title}</h1>
        <hr />
        <p>{this.state.blog.blog_text}</p>
      </div>
    );
  }
}

export default Blog;
