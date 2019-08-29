import React, { Component } from 'react';
import './App.css';
import getData from './parsed-data/data.js'

import { Player } from './player'
import { FilterBar } from './filter-bar'
import { FilterBox } from './filter-box'
import { FilterControls } from './filter-controls'
import { TabControls } from './tab-controls'

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
      DST: true,
      activeTab: 'available',
      searchTerm: ''
    }
    this.togglePlayer = this.togglePlayer.bind(this)
    this.onCheckChange = this.onCheckChange.bind(this)
    this.onSearchChange = this.onSearchChange.bind(this)
    this.changeTab = this.changeTab.bind(this)
    this.setAllFilterBoxes = this.setAllFilterBoxes.bind(this)
  }
  componentDidMount () {
    let temp_data = getData()
    let players = []
    // initially we will sort these by rank order
    Object.keys(temp_data).forEach(key => {
      let player = temp_data[key]
      player['picked'] = false
      player['myteam'] = false
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
  togglePlayerDraft(i) {
    let tempPlayers = this.state.players
    tempPlayers[i].myteam = !tempPlayers[i].myteam
    this.setState({
      players: tempPlayers
    })
  }
  setAllFilterBoxes (trueFalse) {
    this.setState({
      RB: trueFalse,
      WR: trueFalse,
      QB: trueFalse,
      TE: trueFalse,
      K: trueFalse,
      PK: trueFalse,
      DST: trueFalse
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
  onSearchChange (newSearchTerm) {
    this.setState({ searchTerm: newSearchTerm.toLowerCase() })
  }
  changeTab (newTab) {
    this.setState({ activeTab: newTab })
  }
  render () {
    const { players, RB, WR, QB, TE, K, PK, DST, activeTab, searchTerm } = this.state
    return (
      <div style={{'padding': '20px'}}>
        <FilterBar handleSearchChange={this.onSearchChange}/>
        <TabControls changeTab={this.changeTab}/>
        <FilterBox filter='RB' checked={RB} onToggle={() => {this.onCheckChange('RB')}}/>
        <FilterBox filter='WR' checked={WR} onToggle={() => {this.onCheckChange('WR')}}/>
        <FilterBox filter='QB' checked={QB} onToggle={() => {this.onCheckChange('QB')}}/>
        <FilterBox filter='TE' checked={TE} onToggle={() => {this.onCheckChange('TE')}}/>
        <FilterBox filter='K' checked={K} onToggle={() => {this.onCheckChange('K')}}/>
        <FilterBox filter='PK' checked={PK} onToggle={() => {this.onCheckChange('PK')}}/>
        <FilterBox filter='DEFENSE' checked={DST} onToggle={() => {this.onCheckChange('DST')}}/>
        <FilterControls setAllFilterBoxes={this.setAllFilterBoxes}></FilterControls>
        <div>
          <span>Showing: <strong>{activeTab}</strong></span>
        </div>
        {
          players.map((player, i) => {
            return (
              <Player
                key={player['player-name']}
                player={player}
                toggleView={() => { this.togglePlayer(i) }}
                toggleDraft={() => { this.togglePlayerDraft(i) }}
                showPosition={this.state[player.position]}
                activeTab={activeTab}
                searchTerm={searchTerm}
                />
              )
          })
        }
      </div>
    )
  }
}

export default App;
