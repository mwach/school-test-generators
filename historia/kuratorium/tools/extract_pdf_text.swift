import Foundation
import PDFKit

// Wyciąga warstwę tekstową z archiwalnych arkuszy konkursowych,
// dzięki czemu można je przeszukiwać przy kalibrowaniu nowych wariantów.
let arguments = CommandLine.arguments
guard arguments.count == 3 else {
    FileHandle.standardError.write("Użycie: extract_pdf_text <katalog-pdf> <katalog-wyjsciowy>\n".data(using: .utf8)!)
    exit(2)
}

let inputDirectory = URL(fileURLWithPath: arguments[1])
let outputDirectory = URL(fileURLWithPath: arguments[2])
let fileManager = FileManager.default
try? fileManager.createDirectory(at: outputDirectory, withIntermediateDirectories: true)

let pdfFiles = (try fileManager.contentsOfDirectory(at: inputDirectory, includingPropertiesForKeys: nil))
    .filter { $0.pathExtension.lowercased() == "pdf" }
    .sorted { $0.lastPathComponent < $1.lastPathComponent }

for file in pdfFiles {
    guard let document = PDFDocument(url: file) else {
        print("BLAD\t\(file.lastPathComponent)\tnie można otworzyć")
        continue
    }
    var pages: [String] = []
    for index in 0..<document.pageCount {
        let text = document.page(at: index)?.string ?? ""
        pages.append("=== strona \(index + 1) ===\n\(text)")
    }
    let body = pages.joined(separator: "\n")
    let characters = body.filter { !$0.isWhitespace }.count
    let name = file.deletingPathExtension().lastPathComponent + ".txt"
    try body.write(to: outputDirectory.appendingPathComponent(name), atomically: true, encoding: .utf8)
    print("OK\t\(file.lastPathComponent)\tstrony=\(document.pageCount)\tznaki=\(characters)")
}
