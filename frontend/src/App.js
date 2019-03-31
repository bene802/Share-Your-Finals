import React, { Component } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import PostList from "./components/PostList";
import Intro from "./components/Intro";
import { getAllPosts, test } from "./components/FunctionList";
import axios from "axios";

class App extends Component {
  state = {
    edit: {
      edit_show: false,
      edit_post: {
        id: 1,
        user_id: 1,
        author: "Mike",
        title: "title1",
        date: "2019-10-10",
        content: "Made by User1"
      }
    },
    posts: [
      {
        id: 1,
        user_id: 1,
        author: "Mike",
        title: "title1",
        date: "2019-10-10",
        content: "Made by User1"
      },
      {
        id: 2,
        user_id: 1,
        author: "Mike",
        title: "title2",
        date: "2019-10-11",
        content: "Made by User1"
      },
      {
        id: 3,
        user_id: 2,
        author: "Jack",
        title: "title3",
        date: "2019-09-10",
        content: "Made by User2"
      }
    ]
  };
  componentWillMount() {
    console.log("start");
    this.getAll();
  }

  getAll = () => {
    console.log("getAll");
    axios
      .get("http://127.0.0.1:5000/posts", {
        headers: { "Content-Type": "application/json" }
      })
      .then(function(response) {
        console.log(response);
        console.log(response.data);
      });
  };

  // Edit Modal - Show
  handleEditShow = post => {
    let edit = this.state.edit;
    edit.edit_post = post;
    edit.edit_show = true;
    this.setState({ edit });
  };

  // Edit Modal - Close
  handleEditClose = () => {
    let edit = this.state.edit;
    edit.edit_show = false;
    this.setState({ edit });
  };

  handleEditSave = post => {
    let posts = [...this.state.posts];
    for (let p of posts) {
      if (p.id == post.id) {
        Object.assign(p, post);
        break;
      }
    }
    this.setState({ posts });
    let edit = this.state.edit;
    edit.edit_show = false;
    this.setState({ edit });
  };

  render() {
    return (
      <React.Fragment>
        <Navbar />
        <div className="container">
          <Intro />
          <main className="container">
            <PostList
              posts={this.state.posts}
              edit={this.state.edit}
              handleEditShow={this.handleEditShow}
              handleEditClose={this.handleEditClose}
              handleEditSave={this.handleEditSave}
            />
          </main>
        </div>
      </React.Fragment>
    );
  }
}

export default App;
