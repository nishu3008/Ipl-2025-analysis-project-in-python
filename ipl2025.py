import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')

# Create IPL 2025 Top Run Scorers Dataset
runs_data = {
    'Player': ['Sai Sudharsan', 'Suryakumar Yadav', 'Virat Kohli', 'Mitchell Marsh', 'Shreyas Iyer'],
    'Team': ['GT', 'MI', 'RCB', 'LSG', 'KKR'],
    'Runs': [759, 717, 657, 600, 580],
    'Matches': [15, 15, 14, 15, 14],
    'Average': [50.6, 47.8, 46.9, 40.0, 41.4],
    'Strike_Rate': [148.5, 165.2, 142.3, 155.8, 138.9]
}

# Create IPL 2025 Top Wicket Takers Dataset
wickets_data = {
    'Player': ['Prasidh Krishna', 'Josh Hazlewood', 'Noor Ahmad', 'Khaleel Ahmed', 'Mohammed Siraj'],
    'Team': ['GT', 'RCB', 'CSK', 'DC', 'RCB'],
    'Wickets': [25, 22, 15, 14, 13],
    'Matches': [15, 14, 13, 12, 14],
    'Economy': [8.2, 7.8, 7.5, 8.5, 8.9],
    'Average': [18.5, 19.2, 22.1, 23.5, 25.3]
}

# Create DataFrames
df_runs = pd.DataFrame(runs_data)
df_wickets = pd.DataFrame(wickets_data)

print("=" * 70)
print("IPL 2025 STATISTICS ANALYSIS")
print("=" * 70)

# ============ BATTING ANALYSIS ============
print("\n📊 TOP 5 RUN SCORERS - IPL 2025")
print("-" * 70)
print(df_runs.to_string(index=False))

# Calculate additional statistics using NumPy
runs_per_match = np.array(df_runs['Runs']) / np.array(df_runs['Matches'])
df_runs['Runs_Per_Match'] = np.round(runs_per_match, 2)

print("\n📈 BATTING STATISTICS:")
print(f"Total Runs (Top 5): {df_runs['Runs'].sum()}")
print(f"Average Runs: {df_runs['Runs'].mean():.2f}")
print(f"Highest Score: {df_runs['Runs'].max()} by {df_runs.loc[df_runs['Runs'].idxmax(), 'Player']}")
print(f"Standard Deviation: {df_runs['Runs'].std():.2f}")

# ============ BOWLING ANALYSIS ============
print("\n" + "=" * 70)
print("🎯 TOP 5 WICKET TAKERS - IPL 2025")
print("-" * 70)
print(df_wickets.to_string(index=False))

# Calculate additional statistics using NumPy
wickets_per_match = np.array(df_wickets['Wickets']) / np.array(df_wickets['Matches'])
df_wickets['Wickets_Per_Match'] = np.round(wickets_per_match, 2)

print("\n📈 BOWLING STATISTICS:")
print(f"Total Wickets (Top 5): {df_wickets['Wickets'].sum()}")
print(f"Average Wickets: {df_wickets['Wickets'].mean():.2f}")
print(f"Best Bowler: {df_wickets.loc[df_wickets['Wickets'].idxmax(), 'Player']} with {df_wickets['Wickets'].max()} wickets")
print(f"Best Economy: {df_wickets['Economy'].min()} by {df_wickets.loc[df_wickets['Economy'].idxmin(), 'Player']}")

# ============ TEAM ANALYSIS ============
print("\n" + "=" * 70)
print("🏆 TEAM-WISE PERFORMANCE")
print("-" * 70)

# Combine team performance
team_runs = df_runs.groupby('Team')['Runs'].sum()
team_wickets = df_wickets.groupby('Team')['Wickets'].sum()
team_performance = pd.DataFrame({
    'Total_Runs': team_runs,
    'Total_Wickets': team_wickets
}).fillna(0)

print(team_performance)

# ============ VISUALIZATIONS ============
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('IPL 2025 - Comprehensive Statistics Analysis', fontsize=16, fontweight='bold')

# 1. Top Run Scorers Bar Chart
ax1 = axes[0, 0]
colors_runs = plt.cm.viridis(np.linspace(0.3, 0.9, len(df_runs)))
bars1 = ax1.bar(df_runs['Player'], df_runs['Runs'], color=colors_runs, edgecolor='black', linewidth=1.5)
ax1.set_title('Top 5 Run Scorers', fontsize=12, fontweight='bold')
ax1.set_xlabel('Player')
ax1.set_ylabel('Total Runs')
ax1.tick_params(axis='x', rotation=45)
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# 2. Top Wicket Takers Bar Chart
ax2 = axes[0, 1]
colors_wickets = plt.cm.plasma(np.linspace(0.3, 0.9, len(df_wickets)))
bars2 = ax2.bar(df_wickets['Player'], df_wickets['Wickets'], color=colors_wickets, edgecolor='black', linewidth=1.5)
ax2.set_title('Top 5 Wicket Takers', fontsize=12, fontweight='bold')
ax2.set_xlabel('Player')
ax2.set_ylabel('Total Wickets')
ax2.tick_params(axis='x', rotation=45)
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# 3. Strike Rate Comparison
ax3 = axes[0, 2]
ax3.scatter(df_runs['Average'], df_runs['Strike_Rate'], s=df_runs['Runs']/2,
            alpha=0.6, c=range(len(df_runs)), cmap='cool', edgecolors='black', linewidth=2)
for i, player in enumerate(df_runs['Player']):
    ax3.annotate(player, (df_runs['Average'][i], df_runs['Strike_Rate'][i]),
                fontsize=8, ha='right')
ax3.set_title('Batting Average vs Strike Rate', fontsize=12, fontweight='bold')
ax3.set_xlabel('Average')
ax3.set_ylabel('Strike Rate')
ax3.grid(True, alpha=0.3)

# 4. Economy Rate Analysis
ax4 = axes[1, 0]
ax4.plot(df_wickets['Player'], df_wickets['Economy'], marker='o',
         linewidth=2, markersize=10, color='red', markerfacecolor='yellow', markeredgecolor='red')
ax4.set_title('Bowlers Economy Rate', fontsize=12, fontweight='bold')
ax4.set_xlabel('Player')
ax4.set_ylabel('Economy Rate')
ax4.tick_params(axis='x', rotation=45)
ax4.grid(True, alpha=0.3)

# 5. Runs Per Match
ax5 = axes[1, 1]
ax5.barh(df_runs['Player'], df_runs['Runs_Per_Match'], color='orange', edgecolor='black', linewidth=1.5)
ax5.set_title('Average Runs Per Match', fontsize=12, fontweight='bold')
ax5.set_xlabel('Runs Per Match')
ax5.set_ylabel('Player')
for i, v in enumerate(df_runs['Runs_Per_Match']):
    ax5.text(v, i, f' {v:.1f}', va='center', fontweight='bold')

# 6. Wickets Per Match
ax6 = axes[1, 2]
ax6.barh(df_wickets['Player'], df_wickets['Wickets_Per_Match'], color='green', edgecolor='black', linewidth=1.5)
ax6.set_title('Average Wickets Per Match', fontsize=12, fontweight='bold')
ax6.set_xlabel('Wickets Per Match')
ax6.set_ylabel('Player')
for i, v in enumerate(df_wickets['Wickets_Per_Match']):
    ax6.text(v, i, f' {v:.2f}', va='center', fontweight='bold')

plt.tight_layout()
plt.show()

# ============ CORRELATION ANALYSIS ============
print("\n" + "=" * 70)
print("📊 CORRELATION ANALYSIS")
print("-" * 70)

# Batting correlation
batting_corr = df_runs[['Runs', 'Average', 'Strike_Rate']].corr()
print("\nBatting Metrics Correlation:")
print(batting_corr)

# Bowling correlation
bowling_corr = df_wickets[['Wickets', 'Economy', 'Average']].corr()
print("\nBowling Metrics Correlation:")
print(bowling_corr)

# ============ EXPORT DATA ============
print("\n" + "=" * 70)
print("💾 Exporting data to CSV files...")
df_runs.to_csv('ipl_2025_top_batsmen.csv', index=False)
df_wickets.to_csv('ipl_2025_top_bowlers.csv', index=False)
print("✅ Files saved: ipl_2025_top_batsmen.csv, ipl_2025_top_bowlers.csv")
print("=" * 70)