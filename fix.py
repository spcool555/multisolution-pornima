import sys

new_content = """  <!-- SERVICES LIST -->
  <section class="section">
    <div class="container">
      <div style="display:grid;gap:2rem;">

        <!-- 1. Traffic -->
        <div id="traffic" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2070&auto=format&fit=crop" alt="Traffic Management" loading="lazy" />
              <span class="project-category">Traffic</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Intelligent Traffic Management (IITMS)</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Urban traffic congestion and inefficient signal control can lead to increased travel times and safety risks. Our advanced intelligent traffic systems resolve this through real-time monitoring and centralized signal automation.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Real-time signal automation</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Centralized traffic control</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Reduced city-wide congestion</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Improved road safety</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 2. Smart City -->
        <div id="smart-city" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=2064&auto=format&fit=crop" alt="Smart City" loading="lazy" />
              <span class="project-category">Infrastructure</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Smart City ICT Infrastructure</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Lack of integrated digital infrastructure prevents efficient urban management. We deploy end-to-end ICT solutions to empower smart city operations and centralized data-driven governance.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Integrated city-wide systems</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Data-driven urban management</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Scalable digital network</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Transparent governance</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 3. CCTV -->
        <div id="cctv" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="cctv surveliance.jpg" alt="Safe City" loading="lazy" />
              <span class="project-category">Surveillance</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Safe City CCTV Surveillance</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Mitigate growing public safety concerns with comprehensive city-wide monitoring. Our IP-based CCTV networks feature centralized command centers and AI-powered management.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Real-time video monitoring</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Increased public security</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>High-resolution imaging</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Accelerated incident response</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 4. Metro -->
        <div id="metro" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="metro.jpg" alt="Metro Rail" loading="lazy" />
              <span class="project-category">Telecom</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Metro Rail ICT Solutions</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Deliver reliable communication and data networks within complex metro rail environments. We build robust telecom and ICT infrastructures tailored for transportation networks.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Station communication systems</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Resilient network backbone</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Reliable transport operations</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Enhanced passenger safety</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 5. Mapping -->
        <div id="mapping" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="urban.png" alt="3D Urban Mapping" loading="lazy" />
              <span class="project-category">Surveying</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">3D & 4D Urban Mapping</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Replace outdated urban data that leads to inefficient planning. Our cutting-edge 3D and 4D mapping solutions offer exceptional accuracy for direct visualization and land development.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Accurate 3D visualization</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Optimized land development</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Advanced urban planning tools</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Efficient infrastructure growth</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 6. Assessment -->
        <div id="assessment" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="https://images.unsplash.com/photo-1506521781263-d8422e82f27a?q=80&w=2070&auto=format&fit=crop" alt="Digital Building" loading="lazy" />
              <span class="project-category">Security</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Digital Building Assessment</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Replace manual safety audits of large buildings with digital solutions. We use advanced sensor deployments for continuous monitoring of structural integrity.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Enhanced building safety</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Automated safety audits</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Structural health monitoring</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Regulatory compliance</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- 7. Towing -->
        <div id="towing" class="project-card fade-in">
          <div class="project-inner">
            <div class="project-image">
              <img src="towing.jpeg" alt="Towing Services" loading="lazy" />
              <span class="project-category">Operations</span>
            </div>
            <div class="project-body">
              <h2 style="font-size:clamp(1.25rem,2.5vw,1.75rem);font-weight:900;color:#0f172a;margin-bottom:1rem;letter-spacing:-0.01em;">Traffic Towing Services</h2>
              <p style="color:#475569;font-size:1rem;line-height:1.8;margin-bottom:1.5rem;">Road obstructions and illegal parking cause severe traffic disruptions. We provide professional traffic towing and parking management in direct collaboration with local law enforcement.</p>
              <h4 style="font-size:0.7rem;font-weight:800;color:#0f172a;text-transform:uppercase;letter-spacing:0.1em;border-bottom:1px solid #f1f5f9;padding-bottom:0.75rem;margin-bottom:1rem;">Project Impact</h4>
              <ul class="project-impact-grid">
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Rapid obstruction removal</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Enforced parking discipline</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Reduced congestion</span></li>
                <li class="impact-item"><svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Improved emergency access</span></li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open('c:/Users/Administrator/Downloads/Hi (2) (1)/Hi/Hi/DMML/services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<!-- SERVICES LIST (Horizontal Scroll) -->' in line:
        start_idx = i
        break
for i in range(len(lines)-1, -1, -1):
    if '<!-- FOOTER -->' in lines[i]:
        end_idx = i - 1
        while lines[end_idx].strip() == '':
            end_idx -= 1
        break

if start_idx != -1 and end_idx != -1:
    lines = lines[:start_idx] + [new_content] + lines[end_idx+1:]
    with open('c:/Users/Administrator/Downloads/Hi (2) (1)/Hi/Hi/DMML/services.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Successfully updated services.html')
else:
    print(f'Error: Could not find bounds. Start={start_idx}, End={end_idx}')
