import re

replacements = {
"capstone.html": [
 ("UAV Air Quality Monitoring System — Ritwij Gautam", "UAV Air Quality Monitoring System | Ritwij Gautam"),
 ("Capstone Project — University of Guelph", "Capstone Project at University of Guelph"),
 ("quality measurements over agricultural environments — designed so the",
  "quality measurements over agricultural environments, designed so the"),
 ("care — it keeps flying the mission.", "care, it keeps flying the mission."),
 ('Sensor interface schematic — ESP32-based data acquisition with I²C sensor integration.',
  'Sensor interface schematic: ESP32-based data acquisition with I²C sensor integration.'),
],
"flonergia.html": [
 ("Hydroponics Farm Control System — Ritwij Gautam", "Hydroponics Farm Control System | Ritwij Gautam"),
 ("Undergraduate Research Assistant — FloNergia — Jan–Jun 2025",
  "Undergraduate Research Assistant at FloNergia, Jan–Jun 2025"),
 ("air-lift farm — replacing a fragile breadboard prototype with a",
  "air-lift farm, replacing a fragile breadboard prototype with a"),
 ('The vertical air-lift farm — nutrient water circulates through the vertical channels for high-density plant cultivation.',
  'The vertical air-lift farm. Nutrient water circulates through the vertical channels for high-density plant cultivation.'),
 ("breadboard — functional, but fragile. Wiring failures were a real",
  "breadboard: functional, but fragile. Wiring failures were a real"),
 ('Close-up of the growing channels — this is what the system is ultimately controlling.',
  'Close-up of the growing channels. This is what the system is ultimately controlling.'),
 ("state — automating fluid circulation without an operator watching",
  "state, automating fluid circulation without an operator watching"),
 ('PCB revision 2 — refined layout and routing.', 'PCB revision 2, refined layout and routing.'),
 ("automating fluid circulation — the redesigned layout improved",
  "automating fluid circulation. The redesigned layout improved"),
],
"index.html": [
 ("Ritwij Gautam — Embedded Systems Portfolio", "Ritwij Gautam | Embedded Systems Portfolio"),
 ("Computer Engineering — University of Guelph", "Computer Engineering at University of Guelph"),
 ("I design and build embedded hardware — taking a project from requirements",
  "I design and build embedded hardware, taking a project from requirements"),
 ("Work experience — FloNergia — Jan–Jun 2025", "Work experience at FloNergia, Jan–Jun 2025"),
 ('Redesigned the control system for a vertical hydroponic air-lift farm — replacing a fragile breadboard prototype with a compact ESP32-based embedded platform and custom PCB.',
  'Redesigned the control system for a vertical hydroponic air-lift farm, replacing a fragile breadboard prototype with a compact ESP32-based embedded platform and custom PCB.'),
 ("Capstone project — 2025/2026", "Capstone project, 2025/2026"),
 ('alt="Placeholder — Two-Channel USB Oscilloscope"', 'alt="Placeholder: Two-Channel USB Oscilloscope"'),
 ('A two-channel, 500kHz-bandwidth signal acquisition device built from scratch — schematic, PCB, and a hybrid interrupt/DMA firmware architecture around an STM32.',
  'A two-channel, 500kHz-bandwidth signal acquisition device built from scratch: schematic, PCB, and a hybrid interrupt/DMA firmware architecture around an STM32.'),
 ('alt="Placeholder — Real-Time PID Temperature Controller"', 'alt="Placeholder: Real-Time PID Temperature Controller"'),
 ("Course project — ENGG4420 Real-Time Systems Design", "Course project, ENGG4420 Real-Time Systems Design"),
],
"oscilloscope.html": [
 ("Two-Channel USB Oscilloscope — Ritwij Gautam", "Two-Channel USB Oscilloscope | Ritwij Gautam"),
 ('alt="Placeholder — final assembled PCB"', 'alt="Placeholder: final assembled PCB"'),
 ("<b>Photo checklist</b> — capture these and drop them into", "<b>Photo checklist</b>: capture these and drop them into"),
 ("hero.svg → hero.jpg</code> — final PCB, top-down, well-lit", "hero.svg → hero.jpg</code>: final PCB, top-down, well-lit"),
 ("schematic.svg → schematic.png</code> — full KiCad schematic view", "schematic.svg → schematic.png</code>: full KiCad schematic view"),
 ("pcb-layout.svg → pcb-layout.png</code> — KiCad routing view or 3D render", "pcb-layout.svg → pcb-layout.png</code>: KiCad routing view or 3D render"),
 ("breadboard.svg → breadboard.jpg</code> — breadboard prototype photo", "breadboard.svg → breadboard.jpg</code>: breadboard prototype photo"),
 ("architecture.svg → architecture.png</code> — interrupt/DMA/main-loop diagram", "architecture.svg → architecture.png</code>: interrupt/DMA/main-loop diagram"),
 ("logic-analyzer.svg → logic-analyzer.png</code> — SPI bus capture screenshot", "logic-analyzer.svg → logic-analyzer.png</code>: SPI bus capture screenshot"),
 ("demo.svg → demo.jpg</code> or <code>.gif</code> — live waveform on LCD or PC plot", "demo.svg → demo.jpg</code> or <code>.gif</code>: live waveform on LCD or PC plot"),
 ("Not an instrument anyone would actually rely on — deliberately", "Not an instrument anyone would actually rely on. Deliberately"),
 ("scoped as an introductory project — but a real one nonetheless: a", "scoped as an introductory project, but a real one nonetheless: a"),
 ("a built-in 12-bit ADC (5 mega-samples/sec — comfortably above the", "a built-in 12-bit ADC (5 mega-samples/sec, comfortably above the"),
 ('alt="Placeholder — full schematic"', 'alt="Placeholder: full schematic"'),
 ('Full schematic — MCU, LCD, ADC input stage, and USB power delivery.', 'Full schematic: MCU, LCD, ADC input stage, and USB power delivery.'),
 ('alt="Placeholder — PCB layout"', 'alt="Placeholder: PCB layout"'),
 ("breadboard using a dev board with the same MCU — the same rule I'd", "breadboard using a dev board with the same MCU, the same rule I'd"),
 ('alt="Placeholder — breadboard prototype"', 'alt="Placeholder: breadboard prototype"'),
 ('Breadboard prototype — validating wiring and firmware before committing to a PCB.', 'Breadboard prototype, validating wiring and firmware before committing to a PCB.'),
 ("and display rendering — the two tasks that actually need", "and display rendering, the two tasks that actually need"),
 ('alt="Placeholder — firmware architecture diagram"', 'alt="Placeholder: firmware architecture diagram"'),
 ('Firmware architecture — DMA-driven sampling, lightweight ISRs, main-loop rendering.', 'Firmware architecture: DMA-driven sampling, lightweight ISRs, main-loop rendering.'),
 ('<div class="snippet-label">ISR pattern — set a flag, do the work in the main loop</div>', '<div class="snippet-label">ISR pattern: set a flag, do the work in the main loop</div>'),
 ("// Debounce, then just flag the event — never render", "// Debounce, then just flag the event, never render"),
 ("timing using a logic analyzer — catching timing and protocol issues", "timing using a logic analyzer, catching timing and protocol issues"),
 ('alt="Placeholder — logic analyzer SPI capture"', 'alt="Placeholder: logic analyzer SPI capture"'),
 ('<li>Proved the wiring and firmware architecture on a breadboard before committing to a PCB spin — the design worked as intended on first board bring-up.</li>',
  '<li>Proved the wiring and firmware architecture on a breadboard before committing to a PCB spin. The design worked as intended on first board bring-up.</li>'),
 ('alt="Placeholder — live demo"', 'alt="Placeholder: live demo"'),
 ('Live demo — waveform streaming to the LCD and PC in real time.', 'Live demo: waveform streaming to the LCD and PC in real time.'),
],
"rtos-controller.html": [
 ("Real-Time PID Temperature Controller — Ritwij Gautam", "Real-Time PID Temperature Controller | Ritwij Gautam"),
 ("Course project — ENGG4420 Real-Time Systems Design", "Course project, ENGG4420 Real-Time Systems Design"),
 ('<b>Repo link</b> — add a', '<b>Repo link</b>: add a'),
 ('alt="Placeholder — STM32F4 board and LCD"', 'alt="Placeholder: STM32F4 board and LCD"'),
 ("<b>Photo checklist</b> — capture these and drop them into", "<b>Photo checklist</b>: capture these and drop them into"),
 ("hero.svg → hero.jpg</code> — STM32F4 board + LCD, powered on, showing live values", "hero.svg → hero.jpg</code>: STM32F4 board + LCD, powered on, showing live values"),
 ("architecture.svg → architecture.png</code> — task diagram: DDC control, display, input, and clock tasks and how they share data",
  "architecture.svg → architecture.png</code>: task diagram showing DDC control, display, input, and clock tasks and how they share data"),
 ("lcd-closeup.svg → lcd-closeup.jpg</code> — close-up of the LCD readout (setpoint / process variable / controller output)", "lcd-closeup.svg → lcd-closeup.jpg</code>: close-up of the LCD readout (setpoint / process variable / controller output)"),
 ("response-graph.svg → response-graph.png</code> — setpoint step-response plot (setpoint vs. time), same style as a P/PD control plot", "response-graph.svg → response-graph.png</code>: setpoint step-response plot (setpoint vs. time), same style as a P/PD control plot"),
 ("teraterm.svg → teraterm.png</code> — TeraTerm/USB session showing live communication with the LabVIEW plant model", "teraterm.svg → teraterm.png</code>: TeraTerm/USB session showing live communication with the LabVIEW plant model"),
 ('alt="Placeholder — task architecture diagram"', 'alt="Placeholder: task architecture diagram"'),
 ('alt="Placeholder — LCD close-up"', 'alt="Placeholder: LCD close-up"'),
 ('alt="Placeholder — TeraTerm session"', 'alt="Placeholder: TeraTerm session"'),
 ('alt="Placeholder — PID step response graph"', 'alt="Placeholder: PID step response graph"'),
],
"styles.css": [
 ("Ritwij Gautam — Portfolio", "Ritwij Gautam Portfolio"),
],
}

for fname, pairs in replacements.items():
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in pairs:
        if old not in content:
            print(f"MISSING in {fname}: {old[:60]}")
        content = content.replace(old, new)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print("done")
