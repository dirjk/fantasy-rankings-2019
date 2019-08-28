import React, { Component } from 'react'

export default class Player extends Component {
    showIfAvailable () {
        const { player, toggleView, toggleDraft, showPosition } = this.props
        const name = player['player-name']
        const bye = player['bye-week']
        const team = player['team-name']
        const { rank, position } = player
        if (!player.picked && !player.myteam && showPosition) {
            return (
                <div style={{'paddingLeft': '2px'}}>
                    <p><span onClick={toggleView}>[x]</span> {rank} <a href='javascript:void(0)' onClick={toggleDraft}>{name}</a> | {position} | {team} | {bye} </p>
                </div>
            )
        } else {
            return ( null )
        }
    }
    showIfPicked () {
        const { player, toggleView, showPosition } = this.props
        const name = player['player-name']
        const bye = player['bye-week']
        const team = player['team-name']
        const { rank, position } = player
        if (player.picked && !player.myteam && showPosition) {
            return (
                <div style={{'paddingLeft': '2px'}}>
                    <p><span onClick={toggleView}>[-]</span> {rank} {name} | {position} | {team} | {bye} </p>
                </div>
            )
        } else {
            return ( null )
        }
    }
    showMyTeam () {
        const { player, toggleDraft, showPosition } = this.props
        const name = player['player-name']
        const bye = player['bye-week']
        const team = player['team-name']
        const { rank, position } = player
        if (!player.picked && player.myteam && showPosition) {
            return (
                <div style={{'paddingLeft': '2px'}}>
                    <p>{rank} <a href='javascript:void(0)' onClick={toggleDraft}>{name}</a> | {position} | {team} | {bye} </p>
                </div>
            )
        } else {
            return ( null )
        }
    }
    render () {
        const { activeTab, searchTerm, player } = this.props
        if ( player['player-name'].toLowerCase().indexOf(searchTerm) === -1) { return null }
        if ( activeTab === 'available') { return this.showIfAvailable() }
        if ( activeTab === 'picked') { return this.showIfPicked() }
        if ( activeTab === 'my team') { return this.showMyTeam() }
        return ( null )
    }
}