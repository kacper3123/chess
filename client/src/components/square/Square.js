import React from "react";

class Square extends React.Component {

state = {
    piece: null
}
render() {
    return (
        <div id={ this.props.id } class="square">
            {this.props.children}
        </div>
    );
}}

export default Square