/*
Simple Tic-Tac-Toe playable in browser.
Run: node tic_tac_toe_node_server.js
Open: http://localhost:3000
No dependencies.
*/

const http = require('http');
const port = 3000;

const page = `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Tic-Tac-Toe (Node.js)</title>
  <style>
    body{font-family:system-ui,Segoe UI,Roboto,Arial;margin:40px;display:flex;flex-direction:column;align-items:center}
    h1{margin:0 0 10px}
    .board{display:grid;grid-template-columns:repeat(3,100px);grid-gap:8px}
    .cell{width:100px;height:100px;display:flex;align-items:center;justify-content:center;font-size:48px;background:#f0f0f0;cursor:pointer;user-select:none}
    .cell.disabled{cursor:default;opacity:0.7}
    .controls{margin-top:16px}
    button{padding:8px 12px;margin-right:8px}
    .status{margin-top:12px}
  </style>
</head>
<body>
  <h1>Tic-Tac-Toe</h1>
  <div class="board" id="board"></div>
  <div class="controls">
    <button id="newBtn">New Game</button>
    <label>Play as: <select id="playerSelect"><option value="X">X (you)</option><option value="O">O (you)</option></select></label>
    <label style="margin-left:12px">Difficulty: <select id="difficulty"><option value="easy">Easy</option><option value="hard">Hard (Minimax)</option></select></label>
  </div>
  <div class="status" id="status"></div>

  <script>
    const boardEl = document.getElementById('board');
    const statusEl = document.getElementById('status');
    const newBtn = document.getElementById('newBtn');
    const playerSelect = document.getElementById('playerSelect');
    const difficulty = document.getElementById('difficulty');

    let board = Array(9).fill('');
    let human = 'X';
    let ai = 'O';
    let turn = 'X'; // who moves next
    let gameOver = false;

    const wins = [
      [0,1,2],[3,4,5],[6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]
    ];

    function render(){
      boardEl.innerHTML = '';
      board.forEach((v,i)=>{
        const cell = document.createElement('div');
        cell.className = 'cell' + (v? ' disabled':'');
        cell.textContent = v;
        cell.addEventListener('click', ()=> onClick(i));
        boardEl.appendChild(cell);
      });
      if(gameOver){
        boardEl.querySelectorAll('.cell').forEach(c=>c.classList.add('disabled'));
      }
    }

    function onClick(i){
      if(gameOver) return;
      if(board[i]) return;
      if(turn !== human) return;
      board[i] = human;
      turn = ai;
      nextStep();
    }

    function nextStep(){
      const winner = checkWinner(board);
      if(winner || board.every(Boolean)){
        endGame(winner);
        return;
      }
      if(turn === ai){
        if(difficulty.value === 'easy'){
          aiMoveEasy();
        } else {
          aiMoveMinimax();
        }
        turn = human;
        const winner2 = checkWinner(board);
        if(winner2 || board.every(Boolean)){
          endGame(winner2);
          return;
        }
      }
      render();
      updateStatus();
    }

    function aiMoveEasy(){
      // first take winning move, then block, else random
      for(let i=0;i<9;i++){
        if(!board[i]){
          board[i]=ai;
          if(checkWinner(board)===ai) return;
          board[i]='';
        }
      }
      for(let i=0;i<9;i++){
        if(!board[i]){
          board[i]=human;
          if(checkWinner(board)===human){ board[i]=ai; return; }
          board[i]='';
        }
      }
      const empty = board.map((v,i)=> v? null: i).filter(x=>x!==null);
      const pick = empty[Math.floor(Math.random()*empty.length)];
      board[pick]=ai;
    }

    function aiMoveMinimax(){
      const best = minimax(board.slice(), ai);
      board[best.index]=ai;
    }

    function checkWinner(b){
      for(const [a,c,d] of wins){
        if(b[a] && b[a]===b[c] && b[a]===b[d]) return b[a];
      }
      return null;
    }

    function endGame(winner){
      gameOver = true;
      render();
      if(winner){
        statusEl.textContent = (winner===human) ? 'You win' : (winner===ai ? 'Computer wins' : 'Unknown');
      } else {
        statusEl.textContent = 'Draw';
      }
    }

    function updateStatus(){
      if(gameOver) return;
      statusEl.textContent = (turn===human) ? 'Your move' : 'Computer thinking...';
    }

    function newGame(){
      board = Array(9).fill('');
      human = playerSelect.value;
      ai = (human==='X')? 'O':'X';
      turn = 'X';
      gameOver = false;
      statusEl.textContent = '';
      render();
      // if AI starts
      if(turn !== human){
        if(difficulty.value==='easy') aiMoveEasy(); else aiMoveMinimax();
        turn = human;
      }
      render();
      updateStatus();
    }

    // Minimax implementation
    function minimax(b, player){
      const winner = checkWinner(b);
      if(winner===ai) return {score: 10};
      if(winner===human) return {score: -10};
      if(b.every(Boolean)) return {score: 0};

      const moves = [];
      for(let i=0;i<9;i++){
        if(!b[i]){
          const move = {index: i};
          b[i] = player;
          const result = minimax(b, player===ai ? human : ai);
          move.score = result.score;
          b[i] = '';
          moves.push(move);
        }
      }

      let bestMove;
      if(player===ai){
        let bestScore = -Infinity;
        for(const m of moves){ if(m.score>bestScore){ bestScore=m.score; bestMove=m; } }
      } else {
        let bestScore = Infinity;
        for(const m of moves){ if(m.score<bestScore){ bestScore=m.score; bestMove=m; } }
      }
      return bestMove;
    }

    newBtn.addEventListener('click', newGame);
    playerSelect.addEventListener('change', newGame);
    difficulty.addEventListener('change', newGame);

    // initial
    newGame();
  </script>
</body>
</html>
`;

const server = http.createServer((req,res)=>{
  if(req.url === '/' || req.url === '/index.html'){
    res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
    res.end(page);
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(port, ()=>{
  console.log(`Tic-Tac-Toe server running at http://localhost:${port}`);
});
