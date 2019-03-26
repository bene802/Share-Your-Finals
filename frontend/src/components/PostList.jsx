import React, { Component } from "react";
import Post from "./Post";
import EditModal from "../components/EditModal";
import Button from "react-bootstrap/Button";

class PostList extends Component {
  render() {
    return (
      <React.Fragment>
        <div>
          {this.props.posts.map(post => (
            <Post
              key={post.id}
              post={post}
              handleEditShow={this.props.handleEditShow}
              editShow={this.props.editShow}
            />
          ))}
        </div>
        <EditModal
          show={this.props.editShow}
          handleEditClose={this.props.handleEditClose}
        />
      </React.Fragment>
    );
  }
}
export default PostList;
