import React, { Component } from "react";
import axios from "axios";

const getAllPosts = () => {
  return axios
    .get("http://127.0.0.1:5000/posts")
    .then(response => console.log(response));
};

export default getAllPosts;
