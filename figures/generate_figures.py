#!/usr/bin/env python3
"""Generate AetherFlow figures using matplotlib."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyBboxPatch

# Figure 1 — Dynamic Conflict Window
def fig1_conflict_window():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    tau = np.linspace(0.1, 10, 50)
    delta = np.linspace(0.1, 1.0, 50)
    Tau, Delta = np.meshgrid(tau, delta)
    
    lam = 0.5
    W = 1 - np.exp(-lam * Delta * Tau)
    
    surf = ax.plot_surface(Tau, Delta, W, cmap='Greens', alpha=0.8, edgecolor='none')
    
    ax.set_xlabel('Temporal Distance τ(cᵢ, cⱼ)', fontsize=10)
    ax.set_ylabel('Overlap Δ(cᵢ, cⱼ)', fontsize=10)
    ax.set_zlabel('P(Conflict)', fontsize=10)
    ax.set_title('Figure 1 — Dynamic Conflict Window', fontsize=12, fontweight='bold', pad=20)
    
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.tight_layout()
    plt.savefig('fig1_conflict_window.png', dpi=150, bbox_inches='tight', facecolor='#f7f3ec')
    plt.close()
    print('✅ fig1_conflict_window.png')

# Figure 2 — Post-Merge Verification Operator
def fig2_verification_operator():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    nodes = {
        'c_i': (5, 8),
        'c_{i-1}': (3, 6),
        'c_{i-2}': (7, 6),
        'c_{i-3}': (3, 4),
        'c_{i-4}': (7, 4),
        'c_0': (5, 2),
    }
    
    edges = [('c_i', 'c_{i-1}'), ('c_i', 'c_{i-2}'), ('c_{i-1}', 'c_{i-3}'), 
             ('c_{i-2}', 'c_{i-4}'), ('c_{i-3}', 'c_0'), ('c_{i-4}', 'c_0')]
    
    for (a, b) in edges:
        ax.annotate('', xy=nodes[b], xytext=nodes[a],
                    arrowprops=dict(arrowstyle='->', color='#2d6a4f', lw=2))
    
    for name, (x, y) in nodes.items():
        circle = plt.Circle((x, y), 0.4, color='#f7f3ec', ec='#1a1a1a', lw=2, zorder=10)
        ax.add_patch(circle)
        ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold', zorder=11)
    
    ax.text(5, 0.8, 'V(cᵢ) = ⊕_V(Δᵢ, {V(p) | p ∈ P(cᵢ)}, CI(cᵢ))', 
            ha='center', fontsize=12, style='italic')
    ax.text(5, 0.3, 'CI results = leaf nodes', ha='center', fontsize=9, color='#5a564f')
    
    ax.set_title('Figure 2 — Post-Merge Verification Operator', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('fig2_verification_operator.png', dpi=150, bbox_inches='tight', facecolor='#f7f3ec')
    plt.close()
    print('✅ fig2_verification_operator.png')

# Figure 3 — Auto-Remediation Bound
def fig3_remediation_bound():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    K = np.arange(1, 13)
    lam_fail = 0.3
    mu_remediate = 1.0
    gamma = 0.15
    
    for T_react, color, label in [(2, '#1a1a1a', 'T_react = 2'), 
                                    (8, '#2d6a4f', 'T_react = 8'), 
                                    (20, '#7fb69e', 'T_react = 20')]:
        P = 1 - (lam_fail / mu_remediate)**K * np.exp(-gamma * T_react)
        ax.plot(K, P, 'o-', color=color, label=label, linewidth=2, markersize=6)
    
    ax.set_xlabel('Agent capacity tier depth K', fontsize=11)
    ax.set_ylabel('Lower bound on P(Remediation)', fontsize=11)
    ax.set_title('Figure 3 — Auto-Remediation Bound', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    plt.savefig('fig3_remediation_bound.png', dpi=150, bbox_inches='tight', facecolor='#f7f3ec')
    plt.close()
    print('✅ fig3_remediation_bound.png')

# Figure 4 — Three Architectural Pillars
def fig4_architecture():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    pillars = [
        ('Lock-Free\nMerge Entry', 2, 4, 'All changesets\nappended directly\n(no queue)', '#2d6a4f'),
        ('Post-Merge\nVerification', 6, 4, 'CI + semantic\nanalysis\n(decoupled)', '#3a7a5f'),
        ('Proactive\nRemediation', 10, 4, 'Auto-revert /\npatch / rewrite\n(seconds)', '#4a8a6f'),
    ]
    
    for label, x, y, desc, color in pillars:
        box = FancyBboxPatch((x - 1.5, y - 1.5), 3, 3.5,
                              boxstyle='round,pad=0.1',
                              facecolor='#f7f3ec', edgecolor=color, lw=2)
        ax.add_patch(box)
        ax.text(x, y + 1, label, ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(x, y - 1, desc, ha='center', va='center', fontsize=8, color='#5a564f')
    
    for i in range(len(pillars) - 1):
        x1 = pillars[i][1] + 1.5
        x2 = pillars[i+1][1] - 1.5
        y = pillars[i][2]
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle='->', color='#1a1a1a', lw=2))
    
    ax.set_title('Figure 4 — Three Architectural Pillars', fontsize=13, fontweight='bold', pad=20)
    ax.text(6, 1, 'One framework, three independent pillars', ha='center', fontsize=10, style='italic', color='#5a564f')
    
    plt.tight_layout()
    plt.savefig('fig4_architecture.png', dpi=150, bbox_inches='tight', facecolor='#f7f3ec')
    plt.close()
    print('✅ fig4_architecture.png')

# Combined Architecture
def combined_architecture():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(6, 9.5, 'AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution', 
            ha='center', fontsize=14, fontweight='bold')
    
    layers = [
        ('Concurrent AI Agents', 8, '#2d6a4f'),
        ('Lock-Free Merge Entry', 6.5, '#3a7a5f'),
        ('Main Reference (Trunk)', 5, '#1a1a1a'),
        ('Post-Merge Verification Layer', 3.5, '#4a8a6f'),
        ('Proactive Remediation Agents', 2, '#7fb69e'),
    ]
    
    for label, y, color in layers:
        box = FancyBboxPatch((2, y - 0.4), 8, 0.8,
                              boxstyle='round,pad=0.1',
                              facecolor='#f7f3ec', edgecolor=color, lw=2)
        ax.add_patch(box)
        ax.text(6, y, label, ha='center', va='center', fontsize=11, fontweight='bold')
    
    for i in range(len(layers) - 1):
        y1 = layers[i][1] - 0.4
        y2 = layers[i+1][1] + 0.4
        ax.annotate('', xy=(6, y2), xytext=(6, y1),
                    arrowprops=dict(arrowstyle='->', color='#2d6a4f', lw=2))
    
    ax.text(11, 5, 'No merge queues\nNo global locks\nAsynchronous', 
            fontsize=9, color='#5a564f', ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('combined_architecture.png', dpi=150, bbox_inches='tight', facecolor='#f7f3ec')
    plt.close()
    print('✅ combined_architecture.png')

if __name__ == '__main__':
    fig1_conflict_window()
    fig2_verification_operator()
    fig3_remediation_bound()
    fig4_architecture()
    combined_architecture()
    print('\n✅ All 5 figures generated.')
