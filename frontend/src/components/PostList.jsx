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
              edit={this.props.edit}
            />
          ))}
        </div>
        <EditModal
          edit={this.props.edit}
          handleEditClose={this.props.handleEditClose}
          handleEditSave={this.props.handleEditSave}
        />
      </React.Fragment>
    );
  }
}
export default PostList;
