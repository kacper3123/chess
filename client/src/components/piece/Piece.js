import React from "react";

class Piece extends React.Component {
    render() {
        return (
            <div class={this.props.piece}></div>
            );
}}

export default Piece