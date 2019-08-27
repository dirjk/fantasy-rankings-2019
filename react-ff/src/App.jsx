import React, { Component } from 'react';
import './App.css';
import getData from './parsed-data/data.js'

import { Player } from './player'
import { FilterBox } from './filter-box'

class App extends Component {
  constructor (props) {
    super(props)
    this.state = {
      players: [],
      RB: true,
      WR: true,
      QB: true,
      TE: true,
      K: true,
      PK: true,
      DST: true
    }
    this.togglePlayer = this.togglePlayer.bind(this)
    this.onCheckChange = this.onCheckChange.bind(this)
  }
  componentDidMount () {
    let temp_data = getData()
    let players = []
    // initially we will sort these by rank order
    Object.keys(temp_data).forEach(key => {
      let player = temp_data[key]
      player['picked'] = false
      players.push(player)
    })
    players.sort((a,b) => {
      return a.rank - b.rank
    })
    this.setState({
      players: players
    })
  }
  togglePlayer(i) {
    let tempPlayers = this.state.players
    tempPlayers[i].picked = !tempPlayers[i].picked
    this.setState({
      players: tempPlayers      
    })
  }
  onCheckChange (filterType) {
    let newState
    if (filterType === 'RB') {
      newState = { RB: !this.state.RB }
    } else if (filterType === 'WR') {
      newState = { WR: !this.state.WR }
    } else if (filterType === 'QB') {
      newState = { QB: !this.state.QB }
    } else if (filterType === 'TE') {
      newState = { TE: !this.state.TE }
    } else if (filterType === 'K') {
      newState = { K: !this.state.K }
    } else if (filterType === 'PK') {
      newState = { PK: !this.state.PK }
    } else if (filterType === 'DST') {
      newState = { DST: !this.state.DST }
    }
    this.setState(newState)
  }
  render () {
    const { players, RB, WR, QB, TE, K, PK, DST } = this.state
    return (
      <div style={{'padding': '2px'}}>
        <FilterBox filter='RB' checked={RB} onToggle={() => {this.onCheckChange('RB')}}/>
        <FilterBox filter='WR' checked={WR} onToggle={() => {this.onCheckChange('WR')}}/>
        <FilterBox filter='QB' checked={QB} onToggle={() => {this.onCheckChange('QB')}}/>
        <FilterBox filter='TE' checked={TE} onToggle={() => {this.onCheckChange('TE')}}/>
        <FilterBox filter='K' checked={K} onToggle={() => {this.onCheckChange('K')}}/>
        <FilterBox filter='PK' checked={PK} onToggle={() => {this.onCheckChange('PK')}}/>
        <FilterBox filter='DEFENSE' checked={DST} onToggle={() => {this.onCheckChange('DST')}}/>
        {
          players.map((player, i) => {
            if (!player.picked && this.state[player.position]) {
              return (<Player player={player} toggleView={() => { this.togglePlayer(i) }} key={player['player-name']}/>)
            } else {
              return null
            }
          })
        }
      </div>
    )
  }
}

export default App;
