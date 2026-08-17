export interface Publisher {
    id: Number;
    publisher: Number;
    cnpj: string;
    address: string;
    phone: string;
    email?: string | null;
    site?: string | null;   
}