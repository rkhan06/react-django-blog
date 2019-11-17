import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";

class BlogList extends React.Component {
  constructor() {
    super();
    this.state = {
      blogs: []
    };
  }
  componentDidMount() {
    axios.get(`/api/blogs`).then(res => {
      console.log(res.data);
      this.setState({
        blogs: res.data
      });
    });
  }
  displayBlogs() {
    let list = [];
    this.state.blogs.map(blog => {
      return list.push(
        <li key={blog.id}>
          <Link to={"/blogs/?id=" + blog.id}>{blog.title}</Link>
        </li>
      );
    });
    return list;
  }
  render() {
    return (
      <div>
        <h1>List of Blogs</h1>
        <hr />
        <ul>
          {this.state.blogs.map(blog => {
            return (
              <li key={blog.id}>
                <h4>
                  <Link to={`/blog/${blog.id}`}>{blog.title}</Link> -- {blog.author.username}
                </h4>
              </li>
            );
          })}
        </ul>
      </div>
    );
  }
}

export default BlogList;
