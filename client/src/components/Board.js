import React from "react";
import Square from "./square/Square";
import Piece from "./piece/Piece";

function Board() {
    return (
        <div id="container">
            <div id="chessBoard">
                <Square id={11}><Piece piece={"br"}/></Square>
                <Square id={12}><Piece piece={"br"}/></Square>
                <Square id={13} />
                <Square id={14} />
                <Square id={15} />
                <Square id={16} />
                <Square id={17} />
                <Square id={18} />
                <div style= {{ clear: "both" }}></div>
                <Square id={21} />
                <Square id={22} />
                <Square id={23} />
                <Square id={24} />
                <Square id={25} />
                <Square id={26} />
                <Square id={27} />
                <Square id={28} />
                <div style={{ clear: "both" }}></div>
                <Square id={31} />
                <Square id={32} />
                <Square id={33} />
                <Square id={34} />
                <Square id={35} />
                <Square id={36} />
                <Square id={37} />
                <Square id={38} />
                <div style={{ clear: "both" }}></div>
                <Square id={41} />
                <Square id={42} />
                <Square id={43} />
                <Square id={44} />
                <Square id={45} />
                <Square id={46} />
                <Square id={47} />
                <Square id={48} />
                <div style={{ clear: "both" }}></div>
                <Square id={51} />
                <Square id={52} />
                <Square id={53} />
                <Square id={54} />
                <Square id={55} />
                <Square id={56} />
                <Square id={57} />
                <Square id={58} />
                <div style={{ clear: "both" }}></div>
                <Square id={61} />
                <Square id={62} />
                <Square id={63} />
                <Square id={64} />
                <Square id={65} />
                <Square id={66} />
                <Square id={67} />
                <Square id={68} />
                <div style={{ clear: "both" }}></div>
                <Square id={71} />
                <Square id={72} />
                <Square id={73} />
                <Square id={74} />
                <Square id={75} />
                <Square id={76} />
                <Square id={77} />
                <Square id={78} />
                <div style={{ clear: "both" }}></div>
                <Square id={81}/>
                <Square id={82} />
                <Square id={83} />
                <Square id={84} />
                <Square id={85} />
                <Square id={86} />
                <Square id={87} />
                <Square id={88} />
                <div style={{ clear: "both" }}></div>
            </div>
        </div>
    );
  }

  export default Board