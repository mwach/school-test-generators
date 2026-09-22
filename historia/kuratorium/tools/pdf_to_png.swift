import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
guard args.count >= 3,
      let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: pdf_to_png.swift <in.pdf> <outDir> [scale]\n".data(using: .utf8)!)
    exit(1)
}
let outDir = URL(fileURLWithPath: args[2], isDirectory: true)
let scale = args.count > 3 ? CGFloat(Double(args[3]) ?? 1.6) : 1.6
try? FileManager.default.createDirectory(at: outDir, withIntermediateDirectories: true)

for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let box = page.bounds(for: .mediaBox)
    let size = NSSize(width: box.width * scale, height: box.height * scale)
    let image = NSImage(size: size)
    image.lockFocus()
    NSColor.white.setFill()
    NSRect(origin: .zero, size: size).fill()
    if let ctx = NSGraphicsContext.current?.cgContext {
        ctx.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: ctx)
    }
    image.unlockFocus()
    guard let tiff = image.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let png = rep.representation(using: .png, properties: [:]) else { continue }
    let out = outDir.appendingPathComponent(String(format: "strona_%02d.png", i + 1))
    try? png.write(to: out)
    print(out.path)
}
